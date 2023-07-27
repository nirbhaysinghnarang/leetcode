from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #recurrence:
        # dp[i] := min number of coins needed to make up amount i
        # dp[i] = min_coin(dp[i-coin]+1) 
        if amount == 0:
            return 0
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(dp[i-c]+1, dp[i])
        return -1 if dp[amount]==float('inf') else dp[amount]


        
