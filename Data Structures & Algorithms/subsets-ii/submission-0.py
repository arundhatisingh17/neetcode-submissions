class Solution:
    def recurBuilder(self, nums: List[int], final_list: List, path: List, idx: int) -> None:
        final_list.append(path[:]) 
        if idx >= len(nums):
            return

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.recurBuilder(nums, final_list, path, i + 1)
            path.pop()

        return

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        final_list = []
        path = []
        nums = sorted(nums)

        self.recurBuilder(nums, final_list, path, 0)

        return final_list
