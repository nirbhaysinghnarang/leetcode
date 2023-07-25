// https://leetcode.com/problems/maximum-difference-between-increasing-elements

class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<2):
            return -1
        max_difference = -1
        min_number = nums[0]
        for num in nums:
            max_difference = max(max_difference, num-min_number)
            min_number = min(min_number, num)
        return max_difference
            