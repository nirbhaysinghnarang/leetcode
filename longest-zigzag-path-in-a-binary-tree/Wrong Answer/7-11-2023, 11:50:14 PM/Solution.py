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
            
            if root.left is None:
                if direction=="L":
                    return 0
                return 1

            if root.right is None:
                if direction=="R":
                    return 0
                return 1

            if direction == "L":
                return max(1+helper(root.right, "R"), helper(root.left, direction))
            return max(1+helper(root.left, "L"), helper(root.right, direction))

        return max(helper(root, "L"), helper(root, "R"))-1