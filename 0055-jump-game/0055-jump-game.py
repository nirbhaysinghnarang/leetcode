class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        n = len(nums)
        dp[n-1] = True

        for i in range(n-2, -1, -1):
            
            jump = nums[i]
            if jump == 0:
                continue
            for j in range(i+1, min(n-1, i+jump)+1):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]

            