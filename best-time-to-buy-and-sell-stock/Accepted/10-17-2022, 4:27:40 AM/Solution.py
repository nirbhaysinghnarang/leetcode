// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        minsofar = prices[0]
        maxp = 0
        
        for price in prices:
            if price<minsofar:
                minsofar=price
            p = price-minsofar
            if p>maxp:
                maxp=p
        return maxp
            
        