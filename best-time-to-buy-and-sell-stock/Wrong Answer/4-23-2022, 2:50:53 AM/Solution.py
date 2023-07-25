// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # no transactions done if prices is strictly decreasing
        # so first check if prices is strictly decreasing
        if(len(prices)<2):
            return 0
        max_profit, min_stock = float('inf'), prices[0]
        for price in prices:
            max_profit = max(max_profit, price-min_stock)
            min_stock = min(min_stock, price)
        return max_profit
        