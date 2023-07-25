// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float('-inf')
        curr_prod = 1
        L = 0
        for R in range(len(nums)):
            curr_prod *= nums[R]
            while curr_prod < max_prod and L<=R:
                curr_prod /= nums[L]
                L+=1

            max_prod = max(curr_prod, max_prod)

        return max_prod

        