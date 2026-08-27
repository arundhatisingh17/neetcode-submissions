class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        bool_arr = [False] * len(nums)
        bool_arr[0] = True

        for i in range(len(nums)):
            if bool_arr[i] == True:
                for j in range(1, nums[i] + 1):
                    if i + j <= len(nums) - 1:
                        bool_arr[i + j] = True

        print(bool_arr)

        return bool_arr[-1]