// https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        def helper(root):
            if not root:
                return 
            arr.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        root_og = root
        for v in arr:
            print(v)
            if root:
                root.val = v
                root.left = None
                root = root.right
            else:
                print("nothere")
                print(v)

        return root_og
            
            

            

