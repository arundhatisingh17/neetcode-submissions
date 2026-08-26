# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recur(self, node: Optional[TreeNode], min_val: int, max_val: int) -> bool:
        if node == None:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return self.recur(node.left, min_val, node.val) and self.recur(node.right, node.val, max_val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root == None:
            return None

        # recursively set the min and max limits to validate a binary search tree
        return self.recur(root.left, -float('inf'), root.val) and self.recur(root.right, root.val, float('inf'))