// https://leetcode.com/problems/maximum-sum-circular-subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        nums.append(nums[0])

        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)

        return maxSum
