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
            if self.findBST(root, complement):
                return True
            return helper(node.left) or helper(node.right)


        return helper(root)
    



    def findBST(self, root, target):
        if not root:
            return False
        if target == root.val:
            return True

        return self.findBST(root.left, target) or self.findBST(root.right, target)

