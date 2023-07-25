// https://leetcode.com/problems/running-sum-of-1d-array

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [nums[0]]
        for x in range(len(nums)):
            if(x!=0):
                ret.append(ret[x-1]+nums[x])
        return ret
        