// https://leetcode.com/problems/subarray-product-less-than-k

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt = 0
        prod = 1
        L = 0
        subarrays = []
        for R in range(len(nums)):
            prod *= nums[R]
            while prod > k:
                prod /= nums[L]
                L+=1

            subarrays.append(nums[L:R])
            cnt+=1
        print(subarrays)
        return cnt

            
