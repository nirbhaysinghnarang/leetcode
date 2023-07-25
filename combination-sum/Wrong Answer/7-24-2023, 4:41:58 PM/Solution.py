// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        combs = []
        
        def dfs(index, path, current):
            if current==target:
                combs.append(path.copy())
                return

            if index>=len(candidates) or current>target:
                return
            path.append(candidates[index])
            current+=candidates[index]
            dfs(index, path, current)
            path.pop()
            current+=candidates[index]
            dfs(index+1, path, current)

        dfs(0,[],0)
        return combs

