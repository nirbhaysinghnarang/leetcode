// https://leetcode.com/problems/insert-into-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #base case, tree is empty:
        if not root:
            return TreeNode(val, None, None)
        
        #tree has one leaf
        if not root.left and not root.left:
            if val > root.val:
                root.right = TreeNode(val, None, None)
            else:
                root.left = TreeNode(val, None, None)
            return root

            if val>root.val:
                root.right = self.insertIntoBST(root.right, val)
            else:
                root.left = self.insertIntoBST(root.left, val)
            return root