// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_length = 1
        left = 0
        right = 1

        while right < len(nums):
            if nums[right] > nums[right - 1]:
                right += 1
            else:
                max_length = max(max_length, right - left)
                left = right
                right += 1

        return max(max_length, right - left)