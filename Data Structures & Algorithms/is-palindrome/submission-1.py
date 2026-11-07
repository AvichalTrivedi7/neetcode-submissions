class Solution:
    def isPalindrome(self, s: str) -> bool:
        sr = "".join([i.lower() for i in s if i.isalnum()])
        return sr == sr[::-1]