// https://leetcode.com/problems/closest-binary-search-tree-value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        nearest = float('inf')

        def dfs(root):
            if not root:
                return 
            
            nonlocal nearest

            if abs(root.val - target) < abs(nearest-target):
                nearest = root.val
            if abs(root.val - target) == abs(nearest-target):
                nearest = min(root.val, nearest) 
           
            if root.val > target:
                dfs(root.left)
            else:
                dfs(root.right)

        dfs(root)
        return nearest