// https://leetcode.com/problems/palindrome-number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        if(x<10):
            return True
        if(x<100):
            return str(x)[0]==str(x%10)
        return str(x)[0]==str(x%10) and self.isPalindrome(int(str(x)[1:-1]))