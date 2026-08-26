# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        level_order = []
        queue = deque()

        if root == None:
            return []

        queue.append(root)

        while queue:
            local_list = []
            for i in range(len(queue)):
                elem = queue.popleft()
                local_list.append(elem.val)
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)

            level_order.append(local_list)
            

        return level_order
