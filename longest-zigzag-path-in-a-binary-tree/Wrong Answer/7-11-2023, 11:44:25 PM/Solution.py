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
            
            if dir == "L":
                return 1+helper(root.right, "R")
            return 1+helper(root.left, "L")

        return max(helper(root, "L"), helper(root, "R"))