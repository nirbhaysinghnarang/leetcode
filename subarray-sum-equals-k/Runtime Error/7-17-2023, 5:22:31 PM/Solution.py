// https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        def dfs(index, val):
            if val == k:
                count+=1
                return

            for end_index in range(index, len(nums)):
                s = 0
                for i in range(index, end_index):
                    s+= nums[i]
                dfs(end_index, s)

        dfs(0,0)
        return count
                