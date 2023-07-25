// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        valDict = {}
        for index, value in enumerate(nums):
            if (target-value) in valDict:
                return [valDict[target-value],index]
            else:
                valDict[value]=index
                
            
                
                