// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = self.sub_arr_sums(nums)
        return (max(res))        
    def sub_arr_sums(self, nums):
        if not nums:
            return 0
        if (len(nums)==1):
            return nums[0]
        return nums[0]+self.sub_arr_sums([nums[1:]])