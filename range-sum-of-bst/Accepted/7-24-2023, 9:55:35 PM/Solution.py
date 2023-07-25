// https://leetcode.com/problems/range-sum-of-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = 0

        def dfs(node):
            if not node:
                return

            if low<=node.val<=high:
                nonlocal s
                s+=node.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return s