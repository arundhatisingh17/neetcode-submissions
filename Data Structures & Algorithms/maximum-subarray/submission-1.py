class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # use kadane's algorithm for this
        currSum = 0
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):

            # at every point, check whether continue or start another subarray
            dp[i] = max(dp[i-1] + nums[i], nums[i])


        return max(dp)
