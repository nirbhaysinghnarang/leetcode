// https://leetcode.com/problems/find-largest-value-in-each-tree-row

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        q = deque()
        if root:
            q.append(root)

        while len(q) > 0:
            level_heap = []
            for _ in range(len(q)):
                cur = q.popleft()
                level_heap.append(cur)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if level_heap:
                arr.append(max(level_heap))

        return arr



        