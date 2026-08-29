class Solution:
    def recurBuilder(self, nums: List[int], idx: int, memo: List[int]) -> int:

        cnt = 1

        if memo[idx] != -1:
            return memo[idx]

        if idx >= len(nums):
            return 0

        for j in range(idx + 1, len(nums)):
            if nums[j] > nums[idx]:
                cnt = max(cnt, self.recurBuilder(nums, j, memo) + 1)
        
        memo[idx] = cnt

        return cnt

    def lengthOfLIS(self, nums: List[int]) -> int:

        maxVal = 0
        memo = [-1] * len(nums)
        
        for i in range(len(nums)):
            cnt = self.recurBuilder(nums, i, memo)
            maxVal = max(maxVal, cnt)

        return maxVal