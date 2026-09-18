class Solution:
    def recurBuilder(self, rem_amt: int, coins: List[int], idx: int, seen: dict) -> int:

        key = (rem_amt, idx)
        if key in seen:
            return seen[key]

        if rem_amt == 0:
            return 1

        if rem_amt < 0:
            return 0

        total = 0
        for i in range(idx, len(coins)):
            total += self.recurBuilder(rem_amt - coins[i], coins, i, seen)

        seen[key] = total

        return total

    def change(self, amount: int, coins: List[int]) -> int:

        coins = sorted(coins)

        seen = {}
        
        # return the total number of combination
        numCoins = self.recurBuilder(amount, coins, 0, seen)
        return numCoins
