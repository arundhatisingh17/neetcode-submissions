# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeHeight(self, node: Optional[TreeNode]) -> int:

        if node == None:
            return 0

        left = self.treeHeight(node.left)
        right = self.treeHeight(node.right)

        return max(left, right) + 1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True
        
        leftHeight = self.treeHeight(root.left)
        rightHeight = self.treeHeight(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False

        x = self.isBalanced(root.left)
        y = self.isBalanced(root.right)

        return (x and y)
