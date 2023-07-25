// https://leetcode.com/problems/max-consecutive-ones

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        ret = 0
        
        while(right<len(nums)):
            while(nums[right]!=0):
                ret+=1
                right+=1
        return ret