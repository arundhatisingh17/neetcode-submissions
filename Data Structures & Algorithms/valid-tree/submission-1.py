class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # build a dictionary out of the adjacency list for O(1) lookups
        if len(edges) == 0:
            return True

        dict_map = {}
        seen = set()

        for i in range(n):
            dict_map[i] = []

        for n1, n2 in edges:
            dict_map[n1].append(n2)
            dict_map[n2].append(n1)

        queue = deque()
        queue.append(0)

        while (queue):
            for i in range(len(queue)):
                node = queue.pop()

                if node in seen:
                    return False
                seen.add(node)

                for elem in dict_map[node]:
                    if elem not in seen:
                        queue.append(elem)

        if len(seen) != n:
            return False

        return True

