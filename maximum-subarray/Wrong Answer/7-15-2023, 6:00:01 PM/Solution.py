// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0 
        L, R = 0,0
        while(R<len(nums)):
            curSum += nums[R]
            if curSum < 0:
                L = R
                curSum = 0 
            if curSum > maxSum:
                maxSum = curSum
            R+=1
        return maxSum