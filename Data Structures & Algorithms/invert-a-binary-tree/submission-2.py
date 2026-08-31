# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invHelper(self, node: Optional[TreeNode]) -> None:

        if node == None:
            return

        if node.left == None and node.right == None:
            return

        temp = node.left
        node.left = node.right
        node.right = temp

        self.invHelper(node.left)
        self.invHelper(node.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root == None:
            return None

        self.invHelper(root)

        return root