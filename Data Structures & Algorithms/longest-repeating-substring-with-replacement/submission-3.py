class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        start = 0
        max_freq = 0
        res = 0
        for end in range(len(s)):
            if s[end] not in count:
                count[s[end]] = 0
            count[s[end]] += 1
            
            max_freq = max(max_freq, count[s[end]])

            if (end - start + 1) - max_freq > k:
                count[s[start]] -= 1
                start += 1
            
            res = max(res, end - start + 1)
            
        return res