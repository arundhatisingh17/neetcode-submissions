class Solution:
    def recurBuilder(self, nums: List[int], local_sum: int, target: int, idx: int, seen_dict: dict) -> int:

        if (idx, local_sum) in seen_dict:
            return seen_dict[(idx, local_sum)]

        if local_sum == target and idx == len(nums):
            seen_dict[(idx, local_sum)] = 1
            return 1

        if (local_sum > target and idx == len(nums)) or (local_sum < target and idx == len(nums)):
            seen_dict[(idx, local_sum)] = 0
            return 0

        result = self.recurBuilder(nums, local_sum + nums[idx], target, idx + 1, seen_dict) + self.recurBuilder(nums, local_sum - nums[idx], target, idx + 1, seen_dict)

        seen_dict[(idx, local_sum)] = result

        return result


    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        seen_dict = {}
        
        local_sum = 0
        cnt = 0
        cnt += self.recurBuilder(nums, local_sum, target, 0, seen_dict)

        return cnt
