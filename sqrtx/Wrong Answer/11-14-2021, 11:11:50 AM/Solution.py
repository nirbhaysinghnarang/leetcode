// https://leetcode.com/problems/sqrtx

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return 0
        if(x<4):
            return 1
        for i in range((x/2)+1):
            if(i*i==x):
                return i
            elif(i*i>x):
                return (i-1)