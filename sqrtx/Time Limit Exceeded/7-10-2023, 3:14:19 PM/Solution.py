// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        l, r = 0, x
        ans = -1
        while(l<=r):
            mid = (l+r)//2
            sq = mid**2
            if(sq==x):
                return mid
            elif(sq>x):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans
