// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            toFind = target-nums[i]
            for j in range(i+1, len(nums)):
                if j==toFind:
                    return [i-1,j-1]
            
                
                