// https://leetcode.com/problems/permutations-ii

from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        perms = []
        def dfs(index, path,d):
            print(d, path)
            if index==len(nums)-1:
                perms.append(path.copy())
                return

            for i in range(len(nums)):
                if i!=index and d[nums[i]]>0:
                    path.append(nums[i])
                    d[nums[i]]-=1
                    dfs(i, path, d)
                    path.pop()
                    d[nums[i]]+=1
        dfs(0,[],dict(Counter(nums)))
        return perms
           
