// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def zigZagDFS(root, direction, score):
            if root is None:
                return score
            if direction=="L":
                return max(zigZagDFS(root.left, "R", score+1), zigZagDFS(root.right, "R", 0))
            return  max(zigZagDFS(root.right, "L", score+1), zigZagDFS(root.left, "L", 0))
        
        return max(zigZagDFS(root, "L", 0), zigZagDFS(root, "R", 0))-1

