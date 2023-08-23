# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        q = deque()

        q.append(root)
        avgs = []
        while q:
            s = 0
            cnt = 0
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    s+=node.val
                    cnt+=1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            avgs.append(s/cnt)
        return avgs
