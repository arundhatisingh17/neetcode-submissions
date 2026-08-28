class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        dp = [1] * len(nums)
        dp[0] = nums[0]
        
        # we will maintain the least value at every index + highest value
        neg_list = [1] * len(nums)
        neg_list[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] * nums[i], nums[i], neg_list[i - 1] * nums[i])
            neg_list[i] = min(nums[i], neg_list[i - 1] * nums[i], dp[i-1] * nums[i])

        return max(dp)

        