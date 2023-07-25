// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        L = 0
        window_set = {}
        window_sum = sum(nums[:k])
        max_sum = window_sum if self.areFreqs1(window_set) else 0

        for R in range(k, len(nums)):
            window_set[nums[R]] = window_set.get(nums[R], 0) + 1
            window_set[nums[L]] -= 1
            if window_set[nums[L]] == 0:
                del window_set[nums[L]]
            window_sum += nums[R] - nums[L]
            L += 1
            if self.areFreqs1(window_set):
                max_sum = max(max_sum, window_sum)

        return max_sum

    def areFreqs1(self, d):
        for key in d:
            if d[key] > 1:
                return False

        return True
