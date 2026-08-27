class Solution:
    def recurHelper(self, nums: List[int], i: int, memo: List) -> bool:

        if memo[i] == True:
            return True
        elif memo[i] == False:
            return False

        if i >= len(nums) - 1:
            return True

        for j in range(1, nums[i] + 1):
            if self.recurHelper(nums, i + j, memo):
                memo[i] = True
                return True     
                
        memo[i] = False
        return False


    def canJump(self, nums: List[int]) -> bool:
        memo = [None] * (len(nums) + 1)
        return self.recurHelper(nums, 0, memo)
        
        