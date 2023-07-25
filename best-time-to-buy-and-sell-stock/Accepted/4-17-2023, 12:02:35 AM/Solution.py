// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        if (len(prices)==1):
            return 0
        if(len(prices)==2):
            return max(prices[1]-prices[0], 0)

        mid = len(prices)//2
        p_l = prices[:mid]
        p_r = prices[mid:]
        sol_l = self.maxProfit(p_l)
        sol_r = self.maxProfit(p_r)

        return max((max(p_r)-min(p_l)), sol_l, sol_r)