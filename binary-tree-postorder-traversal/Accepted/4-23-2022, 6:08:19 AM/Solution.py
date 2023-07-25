// https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.right and not root.left:
            return [root.val]
        if not root.left:
            return self.postorderTraversal(root.right)+[root.val]
        if not root.right:
            return self.postorderTraversal(root.left)+[root.val]
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]        