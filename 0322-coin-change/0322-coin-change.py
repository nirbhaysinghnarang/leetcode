from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        
        memo = {}
        def topDown(coins, amount):
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            memo[amount] = min([topDown(coins, amount-c)+1 for c in coins])
            return memo[amount]
        ans = topDown(coins, amount) 
        return -1 if ans == float('inf') else ans

        
