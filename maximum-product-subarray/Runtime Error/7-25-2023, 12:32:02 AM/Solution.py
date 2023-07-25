// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float('-inf')
        curr_prod = 1
        L = 0
        for R in range(len(nums)):
            if curr_prod = 0:
                curr_prod = nums[R]
            else:
                curr_prod *= nums[R]
            while curr_prod < max_prod and L<=R:
                if nums[L]!=0:
                    curr_prod /= nums[L]
                else:
                    curr_prod = 1
                L+=1


            max_prod = max(curr_prod, max_prod)

        return max_prod

        