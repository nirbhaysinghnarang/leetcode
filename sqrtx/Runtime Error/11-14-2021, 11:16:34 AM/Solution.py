// https://leetcode.com/problems/sqrtx

class Solution(object):
    def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    for i in range(x+1):
        if(x<i*i):
            return i-1
                