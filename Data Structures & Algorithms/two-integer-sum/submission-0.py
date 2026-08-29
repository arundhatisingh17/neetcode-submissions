class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict_map = {}
        
        for i in range(len(nums)):
            if target - nums[i] in dict_map:
                return [dict_map[target - nums[i]], i]
            dict_map[nums[i]] = i
            
        return []