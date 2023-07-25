// https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root, s):
            if root is None:
                return targetSum==0
            
            leftPSum = dfs(root.left, s+root.val)
            rightPSum = dfs(root.right, s+root.val)

            if(root.left is None and root.right is None):
                if leftPSum == targetSum or rightPSum == targetSum:
                    return True
            