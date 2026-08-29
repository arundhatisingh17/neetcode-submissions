"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        dict_map = {}

        # build it out using bfs
        queue = deque()
        queue.append(node)

        if node == None:
            return None

        while queue:
            for i in range(len(queue)):
                n = queue.pop()
                if n not in dict_map:
                    dummy = Node(n.val)
                    dict_map[n] = dummy

                    for n_iter in n.neighbors:
                        if n_iter not in dict_map:
                            dummy_n = Node(n_iter.val)
                            dict_map[n_iter] = dummy_n
                            dummy.neighbors.append(dummy_n)
                            queue.append(n_iter)
                        else:
                            dummy.neighbors.append(dict_map[n_iter])

                else:
                    for n_iter in n.neighbors:
                        if n_iter not in dict_map:
                            dummy_n = Node(n_iter.val)
                            dict_map[n_iter] = dummy_n
                            dict_map[n].neighbors.append(dummy_n)
                            queue.append(n_iter)
                        else:
                            dict_map[n].neighbors.append(dict_map[n_iter])

        return dict_map[node]

