class Solution:
    def recurBuilder(self, m: int, n: int, i: int, j: int, memo: List[List[int]]):

        cnt = 0

        if i == m-1 and j == n-1:
            return 1

        if i > m - 1 or j > n - 1:
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        cnt += self.recurBuilder(m, n, i, j + 1, memo) + self.recurBuilder(m, n, i + 1, j, memo)

        memo[i][j] = cnt

        return cnt

    def uniquePaths(self, m: int, n: int) -> int:

        num_ways = 0

        memo = [[-1] * n for _ in range(m)]
        num_ways = self.recurBuilder(m, n, 0, 0, memo)

        return num_ways