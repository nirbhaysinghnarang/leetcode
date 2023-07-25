// https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getHeight(root):
            if not root:
                return 0
            return (1+getHeight(root.left)[0], 1+getHeight(root.right)[1])


        if not root:
            return True

        return abs(getHeight(root)[0] - getHeight(root)[1]) < 1