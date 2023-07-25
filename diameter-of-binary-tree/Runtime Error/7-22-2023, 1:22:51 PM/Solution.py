// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def dfs(self, root):
        if not root:
            return -1
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        nonlocal ans
        ans = max(ans, 2+left+right)
        return 1 +max(left, right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return ans