// https://leetcode.com/problems/coin-change

import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(start_index, coins_used, run_total):
            if run_total == amount:
                return len(coins_used)

            if run_total>amount:
                return -1
            ans = sys.maxint
            for (i, coin) in enumerate(coins):
                if run_total + coin < amount:
                    coins_used.append(coin)

                    ans = min(ans, dfs(i, coins_used, run_total+coin))
            return ans

        return dfs(0,[],0)
