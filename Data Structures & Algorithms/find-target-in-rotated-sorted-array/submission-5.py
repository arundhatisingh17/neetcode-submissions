class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # breathe, go step-by-step

        left = 0
        right = len(nums) - 1

        while (left < right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # check which half of the array is sorted
            if nums[left] <= nums[mid]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                    if nums[right] == target:
                        return right
                else:
                    left = mid + 1
                    if nums[left] == target:
                        return left

            elif nums[right] >= nums[mid]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                    if nums[left] == target:
                        return left
                else:
                    right = mid - 1
                    if nums[right] == target:
                        return right

        if nums[left] == target:
            return left

        return -1