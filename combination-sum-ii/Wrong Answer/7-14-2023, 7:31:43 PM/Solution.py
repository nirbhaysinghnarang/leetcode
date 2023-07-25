// https://leetcode.com/problems/combination-sum-ii

from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        d = dict(Counter(candidates))
        candidates.sort()
        def dfs(index, path, curr_sum, counter):
            if curr_sum == target:
                combs.append(path.copy())
                return

            if curr_sum > target:
                return

            for i in range(index, len(candidates)):
                if index!=i and d[candidates[i]]!=0:
                    if i>0 and candidates[i]==candidates[i-1]:
                        continue
                    d[candidates[i]]-=1
                    dfs(index, path+[candidates[i]], curr_sum+candidates[i], d)
                    d[candidates[i]]+=1
            
        dfs(0,[],0,d)
        return combs
            

            

        