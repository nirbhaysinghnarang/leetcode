// https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combs = []
        def dfs(index, lst):
            if len(lst)==k:
                combs.append(lst)
                return
            
            for i in range(index+1, n+1):
                dfs(i, lst+[i])

        dfs(0,[])
        return combs