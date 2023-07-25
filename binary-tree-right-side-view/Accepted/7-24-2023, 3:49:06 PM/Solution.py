// https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS add only right child
        q = deque()
        if root:
            q.append(root)

        soln = []

        while(len(q)>0):
            lvl = deque()
            for _ in range(len(q)):
                curr = q.popleft()
                lvl.append(curr.val)
                #do something with current
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
            soln.append(lvl.popleft())
        return soln
