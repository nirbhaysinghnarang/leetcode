class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1 for _ in range(n+1)]
        dp[n] = 0
        dp[n-1] = cost[n-1]
        for i in range(n-2, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        print(dp)
        return min(dp[0], dp[1])
    
   
        
        
       