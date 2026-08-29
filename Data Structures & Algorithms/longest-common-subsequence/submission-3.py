class Solution:
    def recurBuilder(self, text1: str, text2: str, i: int, j: int, dp: int) -> int:

        if i == len(text1) or j == len(text2):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if text1[i] == text2[j]:
            num = self.recurBuilder(text1, text2, i + 1, j + 1, dp) + 1
            dp[i][j] = max(dp[i][j], num)
            return num
        else:
            result = max(self.recurBuilder(text1, text2, i, j + 1, dp), self.recurBuilder(text1, text2, i + 1, j, dp))

        dp[i][j] = result

        return result

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cnt = 0
        dp = [[-1] * len(text2) for _ in range(len(text1))]

        return self.recurBuilder(text1, text2, 0, 0, dp)
