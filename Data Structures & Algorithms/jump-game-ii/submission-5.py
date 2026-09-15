class Solution:
    def recurBuilder(self, nums: List[int], idx: int, seen: dict) -> int:

        if idx >= len(nums) - 1:
            return 0

        if idx in seen:
            return seen[idx]

        best = float('inf')

        for i in range(idx + 1, min(idx + nums[idx], len(nums) - 1) + 1):
            best = min(best, self.recurBuilder(nums, i, seen) + 1)

        seen[idx] = best

        return best

    def jump(self, nums: List[int]) -> int:

        seen = {}
        
        # min positions required to reach last position in array
        val = self.recurBuilder(nums, 0, seen)
        if val == float('inf'):
            return 0

        return val

