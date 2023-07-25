// https://leetcode.com/problems/combination-sum-ii

from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        def dfs(index, path, s, dic):
            print(path)

            if s > target:
                return 
            if s == target:
                if not sorted(path) in combs:
                    combs.append(path)
                    return

            for i in range(len(candidates)):
                if i!=index and dic[candidates[i]]>0:
                    dic[candidates[i]]-=1
                    dfs(i, path + [candidates[i]], s+candidates[i], dic)
                    dic[candidates[i]]+=1
                
        dfs(0,[],0, dict(Counter(candidates)))
        return combs
