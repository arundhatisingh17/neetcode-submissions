class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        final_list = []
        
        # return k closest points
        heap = []
        heapq.heapify(heap)

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]

            dist = (x * x) + (y * y)

            heapq.heappush(heap, (dist, (x, y)))


        for i in range(k):
            dist, tup = heapq.heappop(heap)
            final_list.append(tup)

        return final_list