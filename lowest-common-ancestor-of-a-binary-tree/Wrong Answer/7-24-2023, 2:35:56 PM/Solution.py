// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        print(root)
        if not root:
            return None
        if root is p:
            return p
        if root is q:
            return q

        if root.left is p and root.right is q:
            return root

        if root.right is p and root.left is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p,q)

        if not left:
            return right
        if not right:
            return left
        