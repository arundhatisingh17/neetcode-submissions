class Solution:
    def palHelper(self, s: str, idx_1: int, idx_2: int) -> str:

        while ( 0 <= idx_1 < len(s) and 0 <= idx_2 < len(s) and s[idx_1] == s[idx_2]):
            idx_1 -= 1
            idx_2 += 1

        return s[idx_1 + 1 : idx_2]

    def longestPalindrome(self, s: str) -> str:

        max_len = 0
        dict_map = {}

        for i in range(len(s)):
            odd_str = self.palHelper(s, i, i)
            even_str = self.palHelper(s, i, i + 1)

            max_len = max(max_len, len(odd_str))
            max_len = max(max_len, len(even_str))

            if len(odd_str) == max_len:
                dict_map[max_len] = odd_str

            if len(even_str) == max_len:
                dict_map[max_len] = even_str

        return dict_map[max_len]