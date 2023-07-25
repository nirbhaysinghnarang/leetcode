// https://leetcode.com/problems/leaf-similar-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return getSequence(root1)==getSequence(root2)
    
    def getSequence(root, sequence):
        def isLeaf(root):
            return root.left is None and root.right is None

        if root is None:
            return sequence
        
        if isLeaf(root):
            sequence.append(root)
            return getSequence(None, sequence)

        leftSeq = getSequence(root.left)
        rightSeq = getSequence(root.right)

        return leftSeq.append(rightSeq)

        

        
        