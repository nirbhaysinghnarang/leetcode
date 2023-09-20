# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:

    

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        colTable = defaultdict(list)
        queue = deque()
        queue.append((root, 0))

        while queue:
            node, col =queue.popleft()
            colTable[col].append(node.val)

            if node.left:
                queue.append((node.left, col-1))
            if node.right:
                queue.append((node.right, col+1))

       
        sortedKeys = sorted(colTable.keys())
        return [colTable[x] for x in sortedKeys]
        