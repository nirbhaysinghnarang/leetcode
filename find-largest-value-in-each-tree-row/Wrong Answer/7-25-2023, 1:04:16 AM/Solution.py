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
        if not root:
            q.append(root)

        while len(q) > 0:
            level_heap = []
            print("HERE")
            for _ in range(len(q)):
                cur = q.popleft()
                print(cur)
                heapq.heappush(level_heap, cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            arr.append(heapq.heappop(level_heap))

        return arr



        