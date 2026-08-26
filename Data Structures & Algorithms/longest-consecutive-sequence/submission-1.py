class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        dict_map = {}
        max_len = 0

        for i in range(len(nums)):
            dict_map[nums[i]] = i

        # iterate through nums to record the maximum len
        for key, val in dict_map.items():
            if key - 1 not in dict_map:
                local_len = 1
                local_num = key + 1
                while (local_num in dict_map):
                    local_len += 1
                    local_num += 1

                max_len = max(max_len, local_len)

        return max_len