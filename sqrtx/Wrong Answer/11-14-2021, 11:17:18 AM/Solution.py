// https://leetcode.com/problems/sqrtx

class Solution(object):
    def mySqrt(self,x):
        if not x:
            return 0
        for i in range(x+1):
            if(x<i*i):
                 return i-1
                