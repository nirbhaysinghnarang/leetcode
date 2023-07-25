// https://leetcode.com/problems/powx-n

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if(x>0):
            return self.myPowPositive(x,n)
        return self.myPowNegative(x,n)
    
    
    def myPowPositive(self, x, n):
        if n==0:
            return 1
        if n==1:
            return x
        return x*self.myPowPositive(x,n-1)
    
    
    def myPowNegative(self,x,n):
        if n==0:
            return 1
        if n==1:
            return x
        return x*(1/self.myPowNegative(x,n+1))