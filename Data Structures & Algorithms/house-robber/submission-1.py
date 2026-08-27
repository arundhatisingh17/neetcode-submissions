class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0] * len(nums)

        if len(nums) > 1:
            dp[0] = nums[0]
            dp[1] = max(dp[0], nums[1])
        else:
            return nums[0]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        print(dp)

        return dp[-1]
        