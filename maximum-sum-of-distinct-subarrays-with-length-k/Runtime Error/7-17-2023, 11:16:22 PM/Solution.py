// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        L = 0
        
        window_sum = max_sum
        window_set = set(nums[:k+1])
        max_sum = sum(nums[:k+1]) if len(window_set)==k else 0
        for R in range(k, len(nums)):
            window_set.add(nums[R])
            window_set.remove(nums[L])
            window_sum += nums[R]
            window_sum -= nums[L]
            L+=1
            if len(window_set)==k:
                max_sum = max(max_sum, window_sum)
        return max_sum

