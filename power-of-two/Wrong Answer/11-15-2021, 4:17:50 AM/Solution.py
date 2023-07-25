// https://leetcode.com/problems/power-of-two

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n==1):  return True
        if not n%2: return False
        return self.isPowerOfTwo(n/2)
        