// https://leetcode.com/problems/find-pivot-index

class Solution(object):
    def getRunningSum(self, nums):
        ret = [nums[0]]
        print(ret, nums)
        for x in range(1,len(nums)):
            ret.append(ret[x-1]+nums[x])
        return ret
            
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        runningSum = self.getRunningSum(nums)
        for x in range(len(nums)):
            if(x==0):
                lSum = 0
            else:
                lSum = self.getRunningSum(nums[:x])[-1]
            if(x==len(nums)-1):
                rSum = 0
            else:
                rSum = self.getRunningSum(nums[x+1:])[-1]
           
            if(lSum==rSum):
                return x
        return -1
        
        
   