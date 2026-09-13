class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # minimum distance to connect all the points
        dict_map = {}
        visited = set()

        for i in range(len(points)):
            x, y = points[i]
            dict_map[(x, y)] = float('inf')

        heap = []

        coord_1, coord_2 = points[0]
        dict_map[(coord_1, coord_2)] = 0

        heapq.heappush(heap, (0, coord_1, coord_2))

        while (heap):
            dist, x_coord, y_coord = heapq.heappop(heap)
            if dict_map[(x_coord, y_coord)] < dist:
                continue

            if (x_coord, y_coord) in visited:
                continue
            visited.add((x_coord, y_coord))

            # iterate through the points each time
            for item in points:
                x, y = item
                if (x, y) not in visited:
                    if ((x, y) != (x_coord, y_coord)):
                        new_dist = abs(x - x_coord) + abs(y - y_coord)
                        if new_dist < dict_map[(x, y)]:
                            dict_map[(x, y)] = new_dist
                            heapq.heappush(heap, (new_dist, x, y))
        local_sum = 0
        for key, val in dict_map.items():
            local_sum += val

        return local_sum



