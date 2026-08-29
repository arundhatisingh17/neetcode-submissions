class Solution:

    def recurBuilder(self, s: str, idx_1: int, idx_2: int):

        cnt = 0
        while idx_1 >= 0 and idx_2 < len(s) and s[idx_1] == s[idx_2]:
            cnt += 1
            idx_1 -= 1
            idx_2 += 1

        return cnt

    def countSubstrings(self, s: str) -> int:

        odd_len = 0
        even_len = 0
        
        for i in range(len(s) - 1):
            idx_1 = i
            idx_2 = i + 1

            odd_len += self.recurBuilder(s, idx_1, idx_1)
            even_len += self.recurBuilder(s, idx_1, idx_2)

        extra = self.recurBuilder(s, len(s) - 1, len(s) - 1)

        return odd_len + even_len + extra
        
