# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def helper(node, direction, length):
            if not node:
                return length
            if direction == "L":
                return max(helper(node.left, "R", length + 1), helper(node.right, "L", 1))
            else:
                return max(helper(node.right, "L", length + 1), helper(node.left, "R", 1))
        return max(helper(root, "L", 0)-1, helper(root, "R",0)-1)