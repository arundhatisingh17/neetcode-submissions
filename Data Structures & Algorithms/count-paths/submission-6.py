class Solution:
    def recurBuilder(self, m: int, n: int, i: int, j: int, memo: List[List[int]]) -> int:
        if i >= m or j >= n:
            return 0

        if i == m - 1 and j == n - 1:
            return 1

        if memo[i][j] != -1:
            return memo[i][j]

        b1 = self.recurBuilder(m, n, i + 1, j, memo)
        b2 = self.recurBuilder(m, n, i, j + 1, memo)

        memo[i][j] = b1 + b2

        return b1 + b2

    def uniquePaths(self, m: int, n: int) -> int:

        cntr = 0
        memo = [[-1] * n for _ in range(m)]

        return self.recurBuilder(m, n, 0, 0, memo)


        