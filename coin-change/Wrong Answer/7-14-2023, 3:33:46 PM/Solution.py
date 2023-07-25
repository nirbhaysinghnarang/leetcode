// https://leetcode.com/problems/coin-change

import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(start_index, coins_used, run_total):
            if run_total == amount:
                return len(coins_used)

            if run_total>amount:
                return -1
            ans = -1
            for (i, coin) in enumerate(coins):
                if run_total + coin < amount:
                    coins_used.append(coin)
                    if ans!=-1:
                        ans = min(ans, dfs(i, coins_used, run_total+coin))
                    else:
                        ans = dfs(i, coins_used, run_total+coin)
                    coins_used.pop()

            return ans

        return dfs(0,[],0)
