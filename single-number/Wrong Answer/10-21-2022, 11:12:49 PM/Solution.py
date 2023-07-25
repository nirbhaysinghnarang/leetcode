// https://leetcode.com/problems/single-number

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        
        
        for k in d:
            if(k==1):
                return k