// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not (root.left or  root.right):
            return False
        
        return root.left.val == root.right.val and self.isSymmetric(root.left) and self.isSymmetric(root.right)
