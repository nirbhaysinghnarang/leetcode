// https://leetcode.com/problems/binary-tree-pruning

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        
        if self.containsOne(root.left):
            root.left = self.pruneTree(root.left)
        else:
            root.left = None

        if self.containsOne(root.right):
            root.right = self.pruneTree(root.right)
        else:
            root.right = None

        return root




    def containsOne(self, root):
        if not root:
            return False

        if root.val == 1:
            return True

        return self.containsOne(root.left) or self.containsOne(root.right)