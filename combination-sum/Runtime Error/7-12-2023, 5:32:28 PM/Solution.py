// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        combs = []
        candidates.sort()
        def dfs(index, lst, curr_sum):
            if curr_sum==target:
                combs.append(lst)
                return
            if curr_sum > targer:
                return

            for i in range(index+1, len(candidates)):
                dfs(i, lst+[candidates[i]], curr_sum+candidates[i])

        dfs(0, [])
        return combs


