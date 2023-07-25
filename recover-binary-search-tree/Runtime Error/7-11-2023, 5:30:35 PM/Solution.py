// https://leetcode.com/problems/recover-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.arr = []
        def inorderTraversal(self, root):
            if not root:
                return
            inorderTraversal(root.left)
            self.arr.append(root)
            inorderTraversal(root.right)
        inorderTraversal(root)
        sort = sorted(leaf.val for leaf in self.arr)
        for i in range(len(sort)):
            self.arr[i].val = sort[i]

