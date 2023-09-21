# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #Inductive assumption: minDepth(node) returns correctly the minimum depth for the subtree at [node]
        #base case: None 
        if not root:
            return 0
    
        if not root.left and not root.right:
            #at leaf
            return 1

        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

        #last recursive case: only has one child
        if root.left:
            return 1+self.minDepth(root.left)
        
        if root.right:
            return 1+self.minDepth(root.right)

        
