// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        power_set = set()

        def dfs(start_index, set_so_far):

            if not set_so_far in power_set:
                power_set.add(list(set_so_far.copy()))

            for i in range(start_index, len(nums)):
                if not nums[i] in set_so_far:
                    set_so_far.add(nums[i])
                    dfs(i, set_so_far)

        dfs(0, set([]))
        return list(power_set)
