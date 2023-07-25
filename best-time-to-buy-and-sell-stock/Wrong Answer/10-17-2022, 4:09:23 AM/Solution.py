// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        mn = prices[0]
        mn_idx = 0
        
        for (i, price) in enumerate(prices):
            if price<mn:
                mn = price 
                mn_idx = i
            
        print(mn)
        mx = mn
        
        for j in range(mn_idx, len(prices)):
            if(prices[j]>mx):
                mx = prices[j]
        return max(mx-mn, 0)
            
        