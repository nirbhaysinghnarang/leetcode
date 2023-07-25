// https://leetcode.com/problems/combination-sum-ii

from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        soln = []

        candidates.sort()

        def dfs(index, path_so_far, running_sum):
            if index>=len(candidates) or running_sum > target:
                path_copy = path_so_far.copy()
                if not path_copy in soln and running_sum == target:
                    soln.append(path_copy)
                    return
                else:
                    return 

            
            path_so_far.append(candidates[index])
            running_sum += candidates[index]

            dfs(index+1, path_so_far, running_sum)

            path_so_far.pop()
            running_sum -= candidates[index]

            dfs(index+1, path_so_far, running_sum)

        dfs(0,[],0)
        return soln

            

            

        