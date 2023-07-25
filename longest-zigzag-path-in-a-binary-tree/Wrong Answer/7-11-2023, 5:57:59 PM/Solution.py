// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, currentDir):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 0
            if root.left is None:
                if currentDir=="l":
                    return 0
                return 1
            if root.right is None:
                if currentDir=="r":
                    return 0
                return 1
            if currentDir == "r":
                return 1+helper(root.left,"l")
            return 1+helper(root.right, "r")

        return max(helper(root, "l"), helper(root, "r"))