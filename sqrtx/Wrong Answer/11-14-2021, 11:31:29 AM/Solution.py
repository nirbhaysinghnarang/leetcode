// https://leetcode.com/problems/sqrtx

class Solution(object):
    def mySqrt(self,x):
        if not x:   return 0
        if x==1:    return 1
        left_lim = 1
        right_lim = x//2
        while(left_lim<=right_lim):
            mid = (left_lim +(right_lim-left_lim)// 2)
            temp = mid*mid
            if(temp==x):
                return temp
            if(temp<x):
                ans = mid
                left_lim = mid+1
            else:
                right_lim = mid-1
        return ans