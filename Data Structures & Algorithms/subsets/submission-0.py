class Solution:
    def recurBuilder(self, idx: int, nums: List[int], path: [], final_list: List[int]) -> None:

        final_list.append(path[:])

        if idx >= len(nums):
            return

        for i in range(idx, len(nums)):
            path.append(nums[i])
            self.recurBuilder(i + 1, nums, path, final_list)
            path.remove(nums[i])

        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # last question
        path = []
        final_list = []

        self.recurBuilder(0, nums, path, final_list)

        return final_list