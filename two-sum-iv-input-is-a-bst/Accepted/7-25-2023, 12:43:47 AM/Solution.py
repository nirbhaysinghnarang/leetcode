// https://leetcode.com/problems/two-sum-iv-input-is-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def helper(node):
            if not node:
                return False
            complement = k - node.val
            if self.findBST(root, complement, node):
                return True
            return helper(node.left) or helper(node.right)


        return helper(root)
    



    def findBST(self, root, target, node):
        if not root:
            return False
        if target == root.val and node is not root:
            return True

        if target > root.val:
            return self.findBST(root.right, target, node)

        return self.findBST(root.left, target, node)

