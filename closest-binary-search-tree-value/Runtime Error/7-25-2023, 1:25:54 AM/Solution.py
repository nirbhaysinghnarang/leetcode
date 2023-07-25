// https://leetcode.com/problems/closest-binary-search-tree-value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        min_delta = float('inf')
        closest_vals = []
        def dfs(root):
            if not root:
                return 
            
            nonlocal min_delta
            nonlocal closest_vals
            if abs(root.val - target) < min_delta:
                min_delta = abs(root.val - target)
                closest_vals.append(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return min(closest_val)