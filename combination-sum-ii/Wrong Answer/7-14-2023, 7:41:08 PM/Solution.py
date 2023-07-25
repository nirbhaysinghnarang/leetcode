// https://leetcode.com/problems/combination-sum-ii

from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        d = dict(Counter(candidates))
        def dfs(index, path, curr_sum, counter):
            if curr_sum == target:
                ps = sorted(path.copy())
                if not ps in combs:
                    combs.append(ps)
                return

            if curr_sum > target:
                return

            for i in range(index, len(candidates)):
                if index!=i and d[candidates[i]]!=0:
                    d[candidates[i]]-=1
                    dfs(index, path+[candidates[i]], curr_sum+candidates[i], d)
                    d[candidates[i]]+=1
            
        dfs(0,[],0,d)
        return combs
            

            

        