// https://leetcode.com/problems/powx-n

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n==1:
            return x
        if n<0:
            return x*(1/n)
        
        return x*self.myPow(x,n-1)
        