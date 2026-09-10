"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        dict_map = {}
        curr = head

        if head == None:
            return None

        # a helper method for creating a node
        def createNode(node):
            if node == None:
                return None

            if node in dict_map:
                return dict_map[node]
            else:
                newNode = Node(node.val)
                dict_map[node] = newNode

            return newNode

        while (curr != None):
            n = createNode(curr)
            n.next = createNode(curr.next)
            n.random = createNode(curr.random)

            n = n.next
            curr = curr.next

        return dict_map[head]


