// https://leetcode.com/problems/combination-sum-ii

from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        combs = []



        def dfs(index, path, s, dic):
            if s > target:
                return 
            if s == target:
                combs.append(path)
                return

            for i in range(len(candidates)):
                if i!=index and dic[candidates[i]]>0:
                    dic[candidates[i]]-=1
                    dfs(i, path + [candidates[i]], s+candidates[i], dic)
                
        dfs(0,[],0, Counter(candidates))
        print(Counter(candidates))
        return combs
