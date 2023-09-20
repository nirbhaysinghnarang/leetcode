# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        levelsums = defaultdict(int)
        q = deque()
        q.append((root,1))
        while q:
            c,l = q.popleft()
            levelsums[l]+=c.val
            if c.left:
                q.append((c.left,l+1))
            if c.right:
                q.append((c.right, l+1))
        if(len(levelsums)<k): return -1
        return sorted(levelsums.values(),reverse=True)[k-1]


        