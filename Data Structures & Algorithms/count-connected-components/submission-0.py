class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # last question then go for a shower

        dict_map = {}
        visited = set()

        num_components = 0

        for i in range(n):
            dict_map[i] = []

        for n1, n2 in edges:
            dict_map[n1].append(n2)
            dict_map[n2].append(n1)

        for i in range(n):
            if i not in visited:
                num_components += 1

                queue = deque()
                queue.append(i)

                while queue:
                    for j in range(len(queue)):
                        node = queue.pop()
                        visited.add(node)

                        for nn in dict_map[node]:
                            if nn not in visited:
                                queue.append(nn)

        return num_components
            