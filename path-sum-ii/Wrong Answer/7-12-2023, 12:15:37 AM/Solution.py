// https://leetcode.com/problems/path-sum-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def dfs(root, value, target, path):
            if not root:
                return 
            

            if not root.left and not root.right:
                if value+root.val==target:
                    path.append(root.val)
                    paths.append(path)
                    return
            path.append(root.val)
            dfs(root.left, value+root.val, target,path)
            dfs(root.right, value+root.val, target, path)

        dfs(root, 0, targetSum, [])
        return paths
          