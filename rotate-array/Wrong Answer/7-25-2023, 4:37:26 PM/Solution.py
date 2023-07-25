// https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_rotated = [n for n in nums]

        for (i, n) in enumerate(nums_rotated):
            nums[i] = nums_rotated[(i+k)%len(nums)]
        
