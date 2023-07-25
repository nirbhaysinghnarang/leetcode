// https://leetcode.com/problems/largest-number-at-least-twice-of-others

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxElem = nums[0]
        maxIndex = 0
        for i in range(1,len(nums)):
            if(nums[i]>maxElem):
                maxElem = nums[i]
                maxIndex = i
        for j in range(len(nums)):
            if(j!=maxIndex and 2*nums[j]>maxElem):
                return -1
        return maxIndex