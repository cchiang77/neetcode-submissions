class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                cleaned += char.lower()
        
        return cleaned == cleaned[::-1]  