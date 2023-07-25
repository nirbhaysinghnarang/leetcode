// https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        number = 0

        def dfs(node):
            if not node:
                return 
            nonlocal number
            number+=1
            dfs(node.left)
            dfs(node.right)

        dfs(root)