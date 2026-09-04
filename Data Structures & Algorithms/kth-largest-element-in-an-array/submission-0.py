class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, -1 * nums[i])

        for i in range(k):
            elem = heapq.heappop(heap)

        return -1 * elem