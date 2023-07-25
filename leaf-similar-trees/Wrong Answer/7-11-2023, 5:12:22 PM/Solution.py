// https://leetcode.com/problems/leaf-similar-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        print(self.inorder(root1, []))
        return self.inorder(root1, [])==self.inorder(root2, [])
    
  
    
    def inorder(self, root, sequence):
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            sequence.append(root.val)
            return sequence

        leftSeq = self.inorder(root.left, sequence)
        rightSeq = self.inorder(root.right, sequence)
        return leftSeq + rightSeq

        

        
        