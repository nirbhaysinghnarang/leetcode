// https://leetcode.com/problems/combination-sum-ii

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        combs = []

        def dfs(index, path, s):
            if s > target:
                return 
            if s == target:
                if sorted(path) not in combs: 
                    combs.append(path)
                    return

            for i in range(len(candidates)):
                if i!=index and candidates[i] not in path:
                    dfs(i, path + [candidates[i]], s+candidates[i])
                
        dfs(0,[],0)
        return combs
