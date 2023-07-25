// https://leetcode.com/problems/find-pivot-index

class Solution(object):
    
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        psums = [0]
        for i in range(len(nums)):
		    psums.append(psums[i] + nums[i]);
        for i in range(len(nums)):
            if psums[i] == psums[len(nums)] - psums[i+1]:
                return i
        return -1
        
        
   