// https://leetcode.com/problems/binary-tree-paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(node, path):
            if not node:
                return
            if node.left is None and node.right is None:
                path.append(str(node.val))
                paths.append("->".join(path.copy()))
                path.pop()
                return

            path.append(str(node.val))
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()


        dfs(root, [])
        return paths

            