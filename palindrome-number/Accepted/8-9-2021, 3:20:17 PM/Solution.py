// https://leetcode.com/problems/palindrome-number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        arr = self.numToArr(x)
        if(arr==arr[::-1]):
            return True
        return False
    def numToArr(self,num):
        arr = []
        while(num>0):
            arr.append(str(num%10))
            num = num//10
        return arr