class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = []
        for i in range(len(nums)):
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, nums[i])
            else:
                heapq.heappush(self.heap, nums[i])
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:  
        heapq.heappush(self.heap, val)
        while (len(self.heap) > self.k):
            heapq.heappop(self.heap)

        return self.heap[0]


