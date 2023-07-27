class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.iteration(nums)

    def recursion_with_memo(self, nums):
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


    def iteration(self, nums):
        dp = [-1 for i in range(len(nums)+1)]
        dp[0] = 0
        dp[1] = nums[0]
        for j in range(1,len(nums)):
            dp[j+1] = max(dp[j], dp[j-1]+nums[j])
        return dp[len(nums)]


