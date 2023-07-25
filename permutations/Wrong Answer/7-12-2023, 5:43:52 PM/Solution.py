// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        def dfs(index, lst):
            if len(lst)==len(nums):
                perms.append(lst)
                return

            for i in range(len(nums)):
                if i!=index:
                    lst.append(nums[i])
                    dfs(i, lst)
                    lst.pop()

        dfs(0, [])
        return perms
