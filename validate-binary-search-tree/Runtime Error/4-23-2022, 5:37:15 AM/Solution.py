// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #BST is valid if left.val < root.val && right.val < root.val && left, right are valid.
        
        if not root:
            return True
        if (not root.right) and (not root.left):
            return True
        node_check = root.left.val < root.val and root.right.val > root.val
        return node_check and self.isValidBST(root.left) and self.isValidBST(root.right)