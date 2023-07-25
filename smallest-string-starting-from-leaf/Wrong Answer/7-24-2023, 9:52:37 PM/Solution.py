// https://leetcode.com/problems/smallest-string-starting-from-leaf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        min_string ='z' * 13     

        def dfs(node, current_string):
            if not node:
                return

            if node.right is None and node.left is None:
                current_string+=str(node.val)
                current_string = current_string[::-1]
                nonlocal min_string
                min_string = min(current_string, min_string)
                return

            current_string += chr(ord('a')+node.val)
            dfs(node.left, current_string)
            dfs(node.right, current_string)

        dfs(root, "")
        return min_string

            