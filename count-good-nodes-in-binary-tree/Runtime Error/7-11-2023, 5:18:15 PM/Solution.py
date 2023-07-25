// https://leetcode.com/problems/count-good-nodes-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return helper(root, float('-inf'))
        def helper(root, max_thus_far):
            #returns the number of good nodes
            #state: max_thus_far, keeps track of max node val on this path
            if not root:
                return 0
            if root.val > max_thus_far:
                return 1+helper(root.left, root.val)+helper(root.right, root.val)
            else:
                return helper(root.left, max_thus_far)+helper(root.right, max_thus_far)

    