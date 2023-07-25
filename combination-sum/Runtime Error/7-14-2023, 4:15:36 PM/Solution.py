// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        combs = []
        memo = {}
        def dfs(index, lst, curr_sum):
            if memo[index]:
                return memo[index]
            if curr_sum==target:
                if not sorted(lst) in combs:
                    memo[index]==lst
                    combs.append(lst)
                return
            for (i,edge) in enumerate(candidates):
                if curr_sum<target:
                    dfs(i, lst+[edge], curr_sum+candidates[i])

        dfs(0, [],0)
        return combs


