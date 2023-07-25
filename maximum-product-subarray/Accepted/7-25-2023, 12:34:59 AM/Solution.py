// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = 1
        cur_min = 1
        ans = -math.inf
        
        for x in nums:
            tmp = cur_max
            cur_max = max(x * cur_max, x * cur_min, x)
            cur_min = min(x * cur_min, x * tmp, x)
            ans = max(ans, cur_max)
            
        return ans

        