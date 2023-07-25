// https://leetcode.com/problems/combination-sum-ii

from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        soln = []

        candidates.sort()

        def dfs(index, path_so_far, running_sum):
            if running_sum > target:
                return 
            
            if running_sum == target:
                soln.append(path_so_far.copy())
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i-1]==candidates[i]:
                    continue
                elif candidates[i]+running_sum > target:
                    return 
                
                candidates[i] + running_sum <= target:
                path_so_far.append(candidates[i])
                running_sum += candidates[i]
                dfs(i+1, path_so_far, running_sum)
                path_so_far.pop()
                running_sum -= candidates[i]

        dfs(0,[],0)
        return soln

            

            

        