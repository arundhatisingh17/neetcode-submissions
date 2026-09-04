class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # for binary search - always test it out on an array of length 2 for confirming
        left = 1
        right = max(piles)

        while (left < right):
            mid = (left + right) // 2

            numHours = 0
            # calculate the numHours w this speed
            for i in range(len(piles)):
                numHours += math.ceil(piles[i] / mid)

            if numHours <= h:
                right = mid

            elif numHours > h:
                left = mid + 1

        return left