// https://leetcode.com/problems/permutations-ii

from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        combs = []

        c = dict(Counter(nums))
        print(c)

        def dfs(index, path,d):
            if index==len(nums)-1:
                combs.append(path.copy())
                return
            
            for (i,num) in enumerate(nums):
                if d[num]>0:
                    d[num]-=1
                    dfs(i, path+[num], d)
                    d[num]+=1

        dfs(0,[],c)
        return combs

