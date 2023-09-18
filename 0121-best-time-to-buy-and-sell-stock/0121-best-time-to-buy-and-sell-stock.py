class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        L = 0
        for R in range(1, len(prices)):
            if R<len(prices) and L<len(prices) and prices[R] > prices[L]:
                ret = max(ret, prices[R]-prices[L])
            else:
                L = R
            R+=1

        return ret

       
