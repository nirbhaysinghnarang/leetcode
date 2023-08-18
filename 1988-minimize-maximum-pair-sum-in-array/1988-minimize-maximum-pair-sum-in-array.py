class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        minPairSumRes = 0
        nums.sort()
        L = 0
        R = len(nums)-1
        while L<=R:
            pairSum = nums[L]+nums[R]
            minPairSumRes = max(minPairSumRes, pairSum)
            L+=1
            R-=1
        return minPairSumRes