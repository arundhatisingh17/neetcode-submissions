# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurHelper(self, node: Optional[TreeNode]) -> None:

        if node == None:
            return

        temp = node.left
        node.left = node.right
        node.right = temp

        self.recurHelper(node.left)  
        self.recurHelper(node.right)
        

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == None:
            return None

        self.recurHelper(root)
        return root
