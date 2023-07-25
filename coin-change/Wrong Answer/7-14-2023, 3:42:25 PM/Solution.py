// https://leetcode.com/problems/coin-change

from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def min_coins(coins, amount, sum):
            if sum == amount:
                return 0

            if sum > amount:
                return inf

            ans = inf
            for coin in coins:
                result = min_coins(coins, amount, sum + coin)
                if result == inf:
                    continue
                ans = min(ans, result + 1)
            
            return ans


        res = min_coins(coins, 0,0)
        return -1 if res==inf else res
            
            
