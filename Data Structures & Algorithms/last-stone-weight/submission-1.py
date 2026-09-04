class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []

        for i in range(len(stones)):
            heapq.heappush(heap, -stones[i])
            
        while (len(heap) > 1):
            elem1 = -1 * heapq.heappop(heap)
            elem2 = -1 * heapq.heappop(heap)

            if elem1 > elem2:
                heapq.heappush(heap, -1 * (elem1 - elem2))

        if len(heap) > 0:
            return -1 * heap[0]

        return 0