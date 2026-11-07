class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined = [i.lower() for i in s if i.isalnum()]
        sr = "".join(refined)
        return sr == sr[::-1]