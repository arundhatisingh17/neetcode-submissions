# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurBuilder(self, node: TreeNode, maxVal: int) -> int:

        if node == None:
            return 0

        if node.val < maxVal:
            isGood = 0
        else:
            isGood = 1

        return self.recurBuilder(node.left, max(node.val, maxVal)) + self.recurBuilder(node.right, max(node.val, maxVal)) + isGood

    def goodNodes(self, root: TreeNode) -> int:
        
        # last question, take a shower after this
        if root == None:
            return 0

        left = 0
        right = 0

        ans = self.recurBuilder(root, root.val)

        return ans
