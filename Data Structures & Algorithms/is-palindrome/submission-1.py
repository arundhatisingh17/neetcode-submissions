class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_iter = ""

        for char in s:
            if char.isalnum():
                s_iter += char.lower()

        l = list(s_iter)

        if l == l[::-1]:
            return True

        return False