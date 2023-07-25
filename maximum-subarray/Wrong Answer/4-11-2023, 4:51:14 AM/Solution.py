// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return sum(self.max_subarray_sum(nums))
    def max_subarray_sum(self,arr):
        if not arr:
            return []
        if len(arr) == 1:
            return arr

        midpoint = len(arr) // 2
        leftPt = 0
        rightPt = len(arr) - 1
        left = arr[:midpoint]
        right = arr[midpoint:]

        maxLeftOnly = self.max_subarray_sum(left)
        maxRightOnly = self.max_subarray_sum(right)
        mss_left = sum(maxLeftOnly)
        mss_right = sum(maxRightOnly)
        leftSum = -100
        totalLeft = 0
        start_mid = -1
        for i in range(midpoint, leftPt, -1):
            totalLeft += arr[i]
            if totalLeft > leftSum:
                start_mid = i
                leftSum = totalLeft

        rightSum = -100
        totalRight = 0
        end_mid = -1
        for i in range(midpoint, rightPt+1):
            totalRight += arr[i]
            if totalRight > rightSum:
                rightSum = totalRight
                end_mid = i

        if mss_left > mss_right and mss_left > leftSum + rightSum:
            return maxLeftOnly

        if mss_right > mss_left and mss_right > leftSum + rightSum:
            return maxRightOnly

        return arr[start_mid:end_mid+1]


