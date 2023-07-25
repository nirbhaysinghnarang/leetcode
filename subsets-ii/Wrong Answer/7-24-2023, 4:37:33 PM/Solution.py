// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        def dfs(start_index, res):
            if start_index >= len(nums):
                res_copy = res.copy()
                if not res_copy in power_set:
                    power_set.append(res_copy)
                return

            res.append(nums[start_index])
            dfs(start_index+1, res)
            res.pop()
            dfs(start_index+1, res)

        dfs(0, [])
        return power_set