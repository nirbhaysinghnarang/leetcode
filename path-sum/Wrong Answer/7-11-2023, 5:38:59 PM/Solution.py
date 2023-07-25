// https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sum_so_far):
            if not root:
                return targetSum==0
            if root.left is None and root.right is None:
                return sum_so_far==targetSum
            sum_so_far += root.val
            return dfs(root.left, sum_so_far) or dfs(root.right, sum_so_far)            
        return dfs(root, 0)