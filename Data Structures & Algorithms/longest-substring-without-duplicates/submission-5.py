from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        window_counter = Counter()

        for end in range(len(s)):
            leading = s[end]
            window_counter[leading] += 1
            while window_counter[leading] > 1:
                trailing = s[start]
                window_counter[trailing] -= 1
                start += 1
            longest = max(end - start + 1, longest)

        return longest    