class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #dp[i]: min cost to reach top if u start at step i
        #at each step, there are two decisions:
        #take step or not, or if take then climb either one or two steps

        #dp[i] = min(dp[i+1], cost[i]+ min(dp[i+1], dp[i+2]))

        dp = [-1 for _ in range(len(cost)+2)]
        n = len(cost)
        dp[n] = 0
        dp[n-1] = cost[n-1]
        dp[n-2] = cost[n-2]
        for j in range(n-3, -1, -1):
            dp[j] = cost[j]+min(
                    dp[j+1],
                    dp[j+2]
                )
        return min(dp[0], dp[1])
       