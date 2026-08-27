class Solution:
    def combSumHelper(self, path: List[int], final_list: List, sum_nums: int, target: int, nums: List[int], start: int) -> None:

        if sum_nums == target:
            final_list.append(sorted(path[:]))
            return

        if sum_nums > target:
            return

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.combSumHelper(path, final_list, sum_nums + nums[i], target, nums, i)
            path.pop()

        return final_list

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        final_list = []
        path = []
        sum_nums = 0

        self.combSumHelper(path, final_list, sum_nums, target, nums, 0)

        return list(final_list)
