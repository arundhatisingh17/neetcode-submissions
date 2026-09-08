# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # code out the right side view
        result = []
        queue = deque()

        if root == None:
            return []
        
        queue.append(root)

        while (queue):
            for i in range(len(queue)):
                elem = queue.popleft()
                if elem.left != None:
                    queue.append(elem.left)
                if elem.right != None:
                    queue.append(elem.right)

            result.append(elem.val)

        return result

