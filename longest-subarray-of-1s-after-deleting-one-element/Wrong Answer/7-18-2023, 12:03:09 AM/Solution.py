// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        L = 0
        max_count = 0
        window_set = Counter()
        for R in range(len(nums)):
            window_set[nums[R]]+=1
            didDelete = False
            while window_set[0] > 1:
                L+=1
                window_set[0] -= 1
                didDelete = True
            sz = R-L if didDelete else R-L+1
            max_count = max(max_count, sz)

        return max_count
            
