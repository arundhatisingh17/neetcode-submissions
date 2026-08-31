# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurBuilder(self, preorder: List[int], inorder: List[int], dict_map: dict, left: int, right: int) -> TreeNode:

        if left > right:
            return None

        node = TreeNode(preorder[self.pre_idx])
        idx = dict_map[preorder[self.pre_idx]]
        self.pre_idx += 1

        node.left = self.recurBuilder(preorder, inorder, dict_map, left, idx - 1)
        node.right = self.recurBuilder(preorder, inorder, dict_map, idx + 1, right)

        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        dict_map = {}
        self.pre_idx = 0
        
        # make an inorder map for O(1) lookup
        for i in range(len(inorder)):
            dict_map[inorder[i]] = i

        node = self.recurBuilder(preorder, inorder, dict_map, 0, len(preorder) - 1)
        return node