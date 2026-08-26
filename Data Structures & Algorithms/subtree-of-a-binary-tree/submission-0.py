# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def recurSubtree(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:

        if node1 == None and node2 == None:
            return True

        if node1 == None or node2 == None:
            return False

        if node1.val == node2.val:
            return self.recurSubtree(node1.left, node2.left) and self.recurSubtree(node1.right, node2.right)

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root == None and subRoot == None:
            return True

        if root == None or subRoot == None:
            return False

        if self.recurSubtree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        