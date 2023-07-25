// https://leetcode.com/problems/find-pivot-index

class Solution(object):
    
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lSum = 0
        total = sum(nums)
        
        for i in range(len(nums)):
            rSum = total - lSum - nums[i]
            
            if(rSum == lSum):
                return i
            
            lSum += nums[i]
            
        return -1
        
        
        
   