// https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, p, q):
        if not p and not q:
            return True

        if not p and q:
            return False

        if p and not q:
            return False

        return p.val == q.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return self.isSame(root, subRoot) or self.isSame(root.right, subRoot) or self.isSame(root.left, subRoot)