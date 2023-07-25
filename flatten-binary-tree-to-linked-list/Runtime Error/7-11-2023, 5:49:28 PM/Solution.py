// https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return None
        
        #preorder template

        #do something
        tmp_left = root.left
        tmp_right = root.right

        root.left = None
        root.right = tmp_left
        root.right.right = tmp_right

        self.flatten(root.left.left)
        self.flatten(root.right.left)

        return root

