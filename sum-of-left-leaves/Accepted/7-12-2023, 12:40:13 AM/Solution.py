// https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root, sumSoFar, parent):

            if root is None:
                return sumSoFar
            
            if root.left is None and root.right is None and parent is not None:
                if parent.left == root:
                    return sumSoFar+root.val
                
            return dfs(root.left, sumSoFar, root)+dfs(root.right, sumSoFar, root)

        return dfs(root, 0, None)