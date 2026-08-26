class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0

        # stored characters with corresponding indices
        unique_map = {}
        max_len = 0
        local_sum = 0

        for right in range(len(s)):
            if s[right] in unique_map:
                left = max(unique_map[s[right]] + 1, left)
                local_sum = 0
            
            unique_map[s[right]] = right
            local_sum = right - left + 1
            max_len = max(max_len, local_sum)


        return max_len
