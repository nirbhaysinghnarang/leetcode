// https://leetcode.com/problems/maximum-sum-circular-subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n1 = nums.append(nums[0])
        n2 = nums[1:]
        return max(maxSum(n1,  n2))


        def maxSum(nums):
            maxSum = nums[0]
            curSum = 0

            for n in nums:
                curSum = max(curSum, 0)
                curSum += n
                maxSum = max(maxSum, curSum)

            return maxSum
