// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        
        # nums = [0,0,1,1,1,2,2,3,3,4]
        j = 1 # slover pointer, only move when meet unique number
        for i in range(1, len(nums)): # faster pointer, i will iterate over all element in nums
            if nums[i] != nums[i-1]: # when nums[i] is a unique number, assign it to nums[j]
                nums[j] = nums[i]
                j += 1
        # After for loop, i = 9, j = 5, nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
        # We have to delete duplicates backwards
        for delete_index in range(i, j-1, -1):
            del nums[delete_index]

        return j