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
            if root is None:
                return
            path.append(root.val)
            if root.left is None and root.right is None:
                if value+root.val == target:
                    paths.append(path)
                    return
            else:
                dfs(root.left, value+root.val, target, path)
                dfs(root.right, value+root.val, target, path)
            path.pop()

        dfs(root, 0, targetSum, [])
        return paths