class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0 
        
        for right in range(len(s2)):
            if right - left + 1 == len(s1):
                if sorted(s2[left : right + 1]) == sorted(s1):
                    return True
                left += 1

        return False