# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        levelsums = defaultdict(int)
        q = deque()
        q.append((root, 1))

        while q:
            node, level = q.popleft()
            levelsums[level]+=node.val
            if node.right:
                q.append((node.right, level+1))
            if node.left:
                q.append((node.left, level+1))
        maxLevel = 1
        maxSum = levelsums[1]

        for level in levelsums:
            if levelsums[level] > maxSum:
                maxSum = levelsums[level]
                maxLevel = level
        
        return maxLevel



        
