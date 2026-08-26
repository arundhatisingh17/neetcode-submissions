# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self, node: Optional[TreeNode], ans_list: List) -> None:
        if node == None:
            return

        self.inOrder(node.left, ans_list)
        ans_list.append(node.val)
        self.inOrder(node.right, ans_list)

        return

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # to return the kth smallest value, we can first do an inorder traversal
        ans_list = []
        self.inOrder(root, ans_list)

        return ans_list[k - 1]