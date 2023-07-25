// https://leetcode.com/problems/find-duplicate-subtrees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right) 
        return p is q


    dupTrees = []

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def helper(root):
            if not root:
                return

            if (not root.left and root.right) or (not root.right and root.left):
                return

            if self.sameTree(root.left, root.right):
                dupTrees.append([root.left])

            helper(root.left)
            helper(root.right)

        helper(root)
        return dupTrees


