// https://leetcode.com/problems/valid-perfect-square

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if(x==1):   return True
        for x in range(num//2):
            if (x*x==num):  return True
        return False