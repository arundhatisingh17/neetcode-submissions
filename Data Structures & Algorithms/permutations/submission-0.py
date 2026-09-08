class Solution:
    def recurBuilder(self, nums: List[List[int]], path: List[int], final_list: List[List[int]], bool_list: List[bool]) -> None:

        if len(path) == len(nums):
            final_list.append(path[::])
            return

        for i in range(len(nums)):
            if bool_list[i] == True:
                continue

            path.append(nums[i])
            bool_list[i] = True

            self.recurBuilder(nums, path, final_list, bool_list)

            bool_list[i] = False
            path.remove(nums[i])

    def permute(self, nums: List[int]) -> List[List[int]]:
        
        path = []
        final_list = []
        bool_list = [False] * len(nums)

        self.recurBuilder(nums, path, final_list, bool_list)
        return final_list