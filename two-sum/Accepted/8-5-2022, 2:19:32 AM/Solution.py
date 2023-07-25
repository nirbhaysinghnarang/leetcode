// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            thisNum = nums[i]
            toFind = target-thisNum
            for j in range(i+1, len(nums)):
                if nums[j]==toFind:
                    return [i,j]
        