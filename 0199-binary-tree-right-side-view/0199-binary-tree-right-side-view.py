# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        # def dfs(root):
        #     if not root:
        #         return
        #     arr.append(root.val)
        #     if root.right:
        #         dfs(root.right)
        #     else:
        #         dfs(root.left)
        # dfs(root)
        # return arr

        def bfs(root):
            if not root:
                return []
            q = deque()
            q.append(root)
            arr = []
            while q:
                level = []
                for _ in range(len(q)):
                    curr = q.popleft()
                    if curr.right:
                        q.append(curr.right)
                    if curr.left:
                        q.append(curr.left)
                    level.append(curr.val)
                arr.append(level[0])
            return arr
        return bfs(root)



            