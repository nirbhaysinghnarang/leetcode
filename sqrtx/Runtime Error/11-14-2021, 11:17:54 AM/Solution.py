// https://leetcode.com/problems/sqrtx

class Solution(object):
    def mySqrt(self,x):
        if not x:
            return 0
        if x<2:
            return 1
        for i in range(x+1):
            if(x<i*i):
                return i-1
