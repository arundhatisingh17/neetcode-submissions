class Solution:

    def pathIter(self, nums: List[int], curr_idx: int, h_idx: int, memo: List[int]) -> int:

        if curr_idx == h_idx:
            return nums[curr_idx]

        if curr_idx > h_idx:
            return 0

        if memo[curr_idx] != -1:
            return memo[curr_idx]

        branch = max(self.pathIter(nums, curr_idx + 1, h_idx, memo), nums[curr_idx] + self.pathIter(nums, curr_idx + 2, h_idx, memo))

        memo[curr_idx] = branch

        return branch


    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return nums[0]

        memo1 = [-1] * len(nums)
        memo2 = [-1] * len(nums)

        branch1 = self.pathIter(nums, 0, len(nums) - 2, memo1)
        branch2 = self.pathIter(nums, 1, len(nums) - 1, memo2)

        return max(branch1, branch2)
