# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        visited = set()
        visited.add(root)
        q.append(root)
        minLevel = 1
        maxSum = float('-inf')
        lvl=1

        while q:
            levelSum = 0
            for _ in range(len(q)):
                node = q.popleft()
                visited.add(node)
                levelSum += node.val
                if node.right and node.right not in visited:
                    q.append(node.right)
                if node.left and node.left not in visited:
                    q.append(node.left)
            if levelSum > maxSum:
                maxSum = levelSum
                minLevel = lvl
            lvl+=1
        return minLevel
            