class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.recursion(nums)

    def recursion(self, nums):
        memo = [-1 for _ in range(len(nums))]
        def recur(nums, i):
            if i < 0:
                return 0
            if memo[i] != -1:
                return memo[i]
            res = max(recur(nums, i-2)+nums[i], recur(nums, i-1))
            memo[i] = res
            return memo[i]

        return recur(nums, len(nums)-1)

