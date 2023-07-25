// https://leetcode.com/problems/reverse-integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
       
        isNegative = (x<0)
        x=(-x if isNegative else x)
        rev = 0
        while x>0:
            rev = rev*10 + x%10
            x=x//10
        if rev<-2**31 or rev>2**31-1:
            return 0
        return -rev if isNegative else rev
        