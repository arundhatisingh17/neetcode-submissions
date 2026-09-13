class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        dict_map = {}

        # create an adjacency graph
        adj_graph = {}
        heap = []
        
        # store the least distance to each node here
        for i in range(1, n + 1):
            dict_map[i] = float('inf')

        dict_map[k] = 0

        # create adj graph
        for i in range(len(times)):
            src, dest, time = times[i]
            if src in adj_graph:
                adj_graph[src].append((dest, time))
            else:
                adj_graph[src] = [(dest, time)]

        heapq.heappush(heap, (0, k))

        while (heap):
            time, node = heapq.heappop(heap)
            print(node)
            if dict_map[node] < time:
                continue

            for item in adj_graph.get(node, []):
                dest_n, time_n = item
                if time + time_n < dict_map[dest_n]:
                    dict_map[dest_n] = time + time_n
                    heapq.heappush(heap, (time + time_n, dest_n))

        max_val = 0
        for key, val in dict_map.items():
            max_val = max(max_val, val)

        if max_val == float('inf'):
            return -1

        return max_val
