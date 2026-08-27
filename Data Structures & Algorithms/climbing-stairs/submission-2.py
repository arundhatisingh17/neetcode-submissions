class Solution:
    def recurHelper(self, n: int, memo: List, maxWays: int) -> int:

        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        if memo[n] != -1:
            return memo[n]

        maxWays += self.recurHelper(n - 1, memo, maxWays) + self.recurHelper(n - 2, memo, maxWays)

        memo[n] = maxWays

        return maxWays
        

    def climbStairs(self, n: int) -> int:

        maxWays = 0
        memo = [-1] * (n + 1)

        # number of way = number of times you hit the base case
        return self.recurHelper(n, memo, maxWays)