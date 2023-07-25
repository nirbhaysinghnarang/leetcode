// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # no transactions done if prices is strictly decreasing
        # so first check if prices is strictly decreasing
        
        dec = False
        # O(N)
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                dec = True
                break
        if not dec:
            return 0
        day_to_buy = prices.index(min(prices)) # O(N)
        min_price = min(prices)
        max_price = prices[day_to_buy]
        day_to_sell = -1 # init to -1
        for i in range(day_to_buy,len(prices)):
            if(prices[i]>max_price):
                max_price = prices[i]
                day_to_sell = i
        print(day_to_sell)
        if day_to_sell!=-1:
            return max_price-min_price
        return self.maxProfit(prices[:day_to_buy])
        
        