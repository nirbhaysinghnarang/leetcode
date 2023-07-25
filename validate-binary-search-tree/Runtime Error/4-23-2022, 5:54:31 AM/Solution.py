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
        return self.isValidBSTHelper(root, float('-inf'),float('inf'))
    def isValidBSTHelper(self, root, MIN, MAX):
        if root==null:
            return True
        if(root.val<=MIN or root.val>=MAX):
            return False
        return self.isValidBSTHelper(root.left, MIN, root.val) and self.isValidBSTHelper(root.right, root.val, MAX)
        
        