// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def helper(root, direction):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 1
            
            if direction=="N":
                return 1+max(helper(root.left, "L"), helper(root.right, "R"))

            if direction == "L":
                return max(1+helper(root.right, "R"), helper(root.left, "N"))
            return max(1+helper(root.left, "L"), helper(root.right, "N"))

        return max(helper(root, "N"), helper(root, "N"))-1