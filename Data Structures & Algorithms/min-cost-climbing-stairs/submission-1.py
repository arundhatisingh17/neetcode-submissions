class Solution:
    def recurBuilder(self, cost: List[int], idx: int, total_amount: int, seen: dict) -> int:

        if idx >= len(cost):
            return total_amount

        key = (idx, total_amount)

        if key in seen:
            return seen[key]

        total_amount += cost[idx]
        val = min(self.recurBuilder(cost, idx + 1, total_amount, seen), self.recurBuilder(cost, idx + 2, total_amount, seen))

        seen[key] = val
        return val

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        total_amount = 0

        # maintain the index as the key, corresponding shortest cost as the value
        seen = {}

        # minimum cost to reach the top of the staircase - past last index in cost
        ans = min(self.recurBuilder(cost, 0, total_amount, seen), self.recurBuilder(cost, 1, total_amount, seen))

        return ans
