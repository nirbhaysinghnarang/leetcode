// https://leetcode.com/problems/remove-element

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for elem in nums:
            if elem!=val:
                nums[index] = elem
                index+=1
        return len(nums)
                
        