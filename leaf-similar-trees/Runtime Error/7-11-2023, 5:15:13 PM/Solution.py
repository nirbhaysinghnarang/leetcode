// https://leetcode.com/problems/leaf-similar-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeaves(root1, [])==self.getLeaves(root2, [])
    
  
    
    def getLeaves(self, root):
        if not root:
            return 
        arr = []
        def helper(root):
            if root not None:
                if root.left is None and root.right is None:
                    arr.append(root.val)
                helper(root.left)
                helper(root.right)
        helper(root)
        return arr
        

        
        