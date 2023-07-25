// https://leetcode.com/problems/minimum-size-subarray-sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        l = float('-inf')
        curSum = 0
        for R in range(len(nums)):
            curSum += nums[R]
            while(curSum >= target):
                l = min(R-L+1, l)
                curSum -= nums[L]
                L += 1

        return 0 if l == float('-inf') else l

