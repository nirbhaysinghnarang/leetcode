// https://leetcode.com/problems/combination-sum-ii

from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        soln = []

        candidates.sort()

        def dfs(index, path_so_far, running_sum):
            if index>=len(candidates) or running_sum >= target:
                path_copy = path_so_far.copy()
                if running_sum == target:
                    soln.append(path_copy)                
                return

            for i in range(index, len(candidates)):
                if i > 0 and candidates[i-1]==candidates[i]:
                    continue
                if candidates[i]+running_sum > target:
                    return 
                if candidates[i] + running_sum <= target:
                    path_so_far.append(candidates[i])
                    running_sum += candidates[i]
                    dfs(i+1, path_so_far, running_sum)
                    path_so_far.pop()
                    running_sum -= candidates[i]

        dfs(0,[],0)
        return soln

            

            

        