class Solution:
    def recurBuilder(self, nums: List[int], target: int, idx: int, sum_nums: int) -> bool:

        if idx == len(nums):
            return False

        if sum_nums == target:
            return True

        if sum_nums > target:
            return False

        return (self.recurBuilder(nums, target, idx + 1, sum_nums + nums[idx]) or self.recurBuilder(nums, target, idx + 1, sum_nums))

    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        sum_nums = 0

        return self.recurBuilder(nums, target, 0, sum_nums)