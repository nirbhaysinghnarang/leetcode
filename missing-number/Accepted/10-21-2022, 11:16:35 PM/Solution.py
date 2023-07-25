// https://leetcode.com/problems/missing-number

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        arr = [x for x in range(n+1)]
        for num in arr:
            if num not in nums:
                return num
            