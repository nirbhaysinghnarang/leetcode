// https://leetcode.com/problems/palindrome-number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        n = x
        rev = 0
        while(n):
            rev = rev * 10 + n % 10
            n //= 10
        return x == rev