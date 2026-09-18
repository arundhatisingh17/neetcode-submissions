class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        dict_map = {}
        
        # cheapest price from src to destination with at most k stops
        adj_list = {}
        queue = deque()

        queue.append((src, 0))

        for i in range(n):
            dict_map[i] = float('inf')
        dict_map[src] = 0

        # build out the adjacency list
        for elem in flights:
            src, dest, dist = elem
            if src not in adj_list:
                adj_list[src] = [[dest, dist]]
            else:
                adj_list[src].append([dest, dist])

        num_stops = 0

        print(queue)

        while (queue and num_stops <= k):
            for i in range(len(queue)):
                src, dist = queue.popleft()
                for n in adj_list.get(src, []):
                    node, dist_1 = n
                    new_dist = dist + dist_1

                    if new_dist < dict_map[node]:
                        dict_map[node] = new_dist
                        queue.append((node, new_dist))

            num_stops += 1

        if dict_map[dst] == float('inf'):
            return -1

        return dict_map[dst] 

