// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        soln = []

        if root:
            soln.append([root.val])

        q = deque()

        while len(q) > 0:
            curr_lvl = []
            for _ in range(len(q)):
                curr = q.popleft()
                curr_lvl.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            soln.append(curr_lvl)

        return soln



