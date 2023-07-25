// https://leetcode.com/problems/two-sum-bsts

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        inorder1 = self.inorder(root1)
        inorder2 = self.inorder(root2)

        for num in inorder1:
            com = target - num
            if self.binarySearch(inorder2, com):
                return True

        return False

    

    def inorder(self, root):
        arr = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)

        dfs(root)
        return arr


    def binarySearch(self, arr, target):
        L, R = 0, len(arr)-1
        while L<=R:
            mid = (L+R)//2
            if arr[mid]==target:
                return True
            if mid>target:
                R = mid-1
            else:
                L = mid+1

        return False