// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        L = 0
        max_count = 0
        window_set = Counter()
        for R in range(len(nums)):
            # increment count
            window_set[nums[R]]+=1
            # keep on moving left ptr until we have at most 1 one in the window
            while window_set[0] > 1:
                window_set[nums[L]] -= 1
                L+=1

            max_count = max(max_count, window_set[1])

        return max_count
            
