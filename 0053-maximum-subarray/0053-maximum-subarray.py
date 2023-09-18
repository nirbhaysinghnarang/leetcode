class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0 
        L, R = 0,0
        for R in range(len(nums)):
            if curSum < 0:
                L = R
                curSum = 0 
            curSum += nums[R]
            if curSum > maxSum:
                maxSum = curSum
        return maxSum