# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        levels = defaultdict(list)
        q = deque()
        q.append((root, 0))

        while q:
            node, level = q.popleft()
            levels[level].append(node.val)
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))

        max_depth = max(levels.keys())

        return levels[max_depth][0]
        

