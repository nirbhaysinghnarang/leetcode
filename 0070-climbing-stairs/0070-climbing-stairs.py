class Solution:
    def climbStairs(self, n: int) -> int:
        #dp[i]:= num of ways to get to the i-th step
        #dp[0]:=1
        #dp[1]:=1
        #dp[i] = dp[i-1]+dp[i-2] for i 
        dp = [-1 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1

        for j in range(2, n+1):
            dp[j] = dp[j-1]+dp[j-2]

        return dp[n]
       