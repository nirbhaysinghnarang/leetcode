from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = []
        def dfs(path, d):
            if all([d[k]==0 for k in d]):
                perms.append(path.copy())
                return
            for k in d:
               if d[k]>0:
                    path.append(k)
                    d[k]-=1
                    dfs(path, d)
                    path.pop()
                    d[k]+=1
        dfs([],dict(Counter(nums)))
        return perms
           
