// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        if len(preorder)==1 and len(inorder)==1:
            return TreeNode(preorder[0],None, None)
        root = preorder[0]
        root_index_in_inorder = inorder.index(root)
        left_children_in_inorder = inorder[:root_index_in_inorder]
        right_children_in_inorder = inorder[root_index_in_inorder:]
        left_children_in_preorder = preorder[:len(left_children_in_inorder)]
        right_children_in_preorder = preorder[len(left_children_in_inorder):]

        left_subtree = self.buildTree(left_children_in_preorder, left_children_in_inorder)
        right_subtree =  self.buildTree(right_children_in_preorder, right_children_in_inorder)
        return TreeNode(val=root, left=left_subtree, right=right_subtree)

