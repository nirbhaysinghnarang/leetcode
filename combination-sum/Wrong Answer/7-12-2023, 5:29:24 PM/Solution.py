// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        combs = []
        candidates.sort()
        def dfs(index, lst):
            if sum(lst)==target:
                if (lst) in combs:
                    combs.append(lst)
                    return
            for (i,edge) in enumerate(candidates):
                if sum(lst)<target:
                    dfs(i, lst+[edge])

        dfs(0, [])
        return combs


