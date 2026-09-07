class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        start = 0
        rem = 0

        for i in range(len(gas)):
            rem = rem + gas[i] - cost[i]
            if rem < 0:
                start = i + 1
                rem = 0

        return start