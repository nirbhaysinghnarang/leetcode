// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        power_set = []


        def dfs(start_index, res):
            if start_index >= len(nums):
                power_set.append(res.copy())
                return

            res.append(nums[start_index])
            dfs(start_index+1, res)
            res.pop()
            dfs(start_index+1, res)

        dfs(0, [])
        return power_set