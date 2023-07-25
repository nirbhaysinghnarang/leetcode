// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        combs = []

        def dfs(index, lst):

            if sum(lst)==target:
                combs.append(lst)
                return

            for (i,edge) in enumerate(candidates):
                if sum(lst)<target:
                    dfs(i, lst+[edge])

        dfs(0, [])
        return combs


