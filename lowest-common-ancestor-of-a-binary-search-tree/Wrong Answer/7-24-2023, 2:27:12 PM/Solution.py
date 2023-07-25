// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        #base case
        if not root:
            return root

        if p is root or q is root:
            return root

        if root.left is p and root.right is q:
            return root

        return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)
        

