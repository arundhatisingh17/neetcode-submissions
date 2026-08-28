class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxFreq = 0
        left = 0
        freq_map = {}

        maxLen = 0
        
        for right in range(len(s)):
            freq_map[s[right]] = freq_map.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freq_map[s[right]])

            if (right - left + 1) - maxFreq > k:
                freq_map[s[left]] -= 1
                left = left + 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen

