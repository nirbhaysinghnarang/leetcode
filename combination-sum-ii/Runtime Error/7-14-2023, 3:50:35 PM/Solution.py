// https://leetcode.com/problems/combination-sum-ii

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        combs = []
        memo = {}

        def dfs(index, path, sum):
            if sum == target:
                if memo.get(path) is None:
                    combs.append(path)
                    return

            for i in range(len(candidates)):
                if i!=index:
                    path.append(candidates[i])
                    sum+=candidates[i]
                    dfs(i, path, sum)
                    memo[path]=True
                    path.pop()
                
        dfs(0,[],0)
        return combs
