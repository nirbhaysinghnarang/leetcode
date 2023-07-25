// https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.left and not root.left:
            return [root.val]
        if not root.left:
            return [root.val]+inorderTraversal(root.right)
        if not root.right:
            return inorderTraversal(root.left)+[root.val]
        return inorderTraversal(root.left)+[root.val]+inorderTraversal(root.right)
        
            