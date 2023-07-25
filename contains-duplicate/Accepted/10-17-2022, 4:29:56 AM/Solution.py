// https://leetcode.com/problems/contains-duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for num in nums:
            if num in d:
                d[num] +=1 
            else:
                d[num] = 1
        print(d)
        return len(d.keys())!=len(nums)
        