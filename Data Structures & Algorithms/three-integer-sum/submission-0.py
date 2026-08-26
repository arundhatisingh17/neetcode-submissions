class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        final_list = set()
        
        for i in range(len(nums)):
            dict_map = {}
            target = 0 - nums[i]
            for j in range(i+1, len(nums)):
                if target - nums[j] in dict_map:
                    final_list.add(tuple(sorted([nums[i], target - nums[j], nums[j]])))
                else:
                    dict_map[nums[j]] = dict_map.get(nums[j], 0) + 1


        return list(final_list)