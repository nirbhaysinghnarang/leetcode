// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = 0
        max_seq = []
        for R in range(1,len(nums)):
            sequence = nums[L:R]
            while not sorted(sequence)==sequence:
                L+=1
                sequence = nums[L:R]


            if len(sequence) > len(max_seq):
                max_seq = sequence

        return len(max_seq)
            




       