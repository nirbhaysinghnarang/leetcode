// https://leetcode.com/problems/combination-sum-ii

from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        c = Counter(candidates)
        candidates.sort()
        def dfs(index, path, s, dic):

            if s > target:
                return 
            if s == target:
                if not sorted(path) in combs:
                    combs.append(sorted(path))
                    return
            for i in range(index, len(candidates)):
                if dic[candidates[i]]>0:
                    dic[candidates[i]]-=1
                    dfs(i, path + [candidates[i]], s+candidates[i], dic)
                    dic[candidates[i]]+=1
                
        dfs(0,[],0, dict(c))
        return combs
