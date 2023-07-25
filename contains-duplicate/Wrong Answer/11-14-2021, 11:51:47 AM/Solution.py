// https://leetcode.com/problems/contains-duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return (nums==set(nums))
        