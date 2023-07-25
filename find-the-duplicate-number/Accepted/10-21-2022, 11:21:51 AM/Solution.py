// https://leetcode.com/problems/find-the-duplicate-number

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        
        for num in nums:
            if num in dic:
                return num
            dic[num]="LOL"
        