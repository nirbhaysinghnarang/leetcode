// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for (i, num) in enumerate(nums):
            comp = target-num
            if comp in d:
                return [d[comp], i]
            else:
                d[num] = i
        