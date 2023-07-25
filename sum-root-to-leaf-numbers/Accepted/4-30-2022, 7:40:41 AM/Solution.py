// https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.util(root,0)
        
        
        
        
    def util(self, root, val):
        if not root:
            return 0
        val=val*10+root.val
        if not root.left and not root.right:
            return val
        return self.util(root.left, val)+self.util(root.right, val)
    

    
        
        
        
    
    
        