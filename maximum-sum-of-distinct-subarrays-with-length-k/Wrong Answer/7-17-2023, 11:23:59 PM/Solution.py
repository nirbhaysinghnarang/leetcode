// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k

from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        L = 0
        window_set = dict(Counter(nums[:k]))
        max_sum = sum(nums[:k]) if self.areFreqs1(window_set) else 0
        window_sum = max_sum
        for R in range(k, len(nums)):
            if nums[R] in window_set:
                window_set[nums[R]]+=1
            else:
                window_set[nums[R]]=1
            window_set[nums[L]] = max(0, window_set[nums[L]]-1)
            window_sum += nums[R]
            window_sum -= nums[L]
            L+=1
            print(window_set, window_sum)
            if self.areFreqs1(window_set):
                max_sum = max(max_sum, window_sum)
        return max_sum

    def areFreqs1(self, d):
        for key in d:
            if d[key]>1:
                return False

        return True