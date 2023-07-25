// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        right = 0
        maxes = []
        for left in range(len(nums)):
            max_thus_far = 0
            while(nums[right]>nums[left]):
                max_thus_far+=1
                right+=1
            maxes.append(max_thus_far)


        return max(maxes)
