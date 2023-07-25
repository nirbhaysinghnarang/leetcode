// https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, p, q):
        if p and q:
            return p.val == q.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
        return p is q

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSame(root, subRoot):
            return True
            
        return self.isSame(root.right, subRoot) or self.isSame(root.left, subRoot)