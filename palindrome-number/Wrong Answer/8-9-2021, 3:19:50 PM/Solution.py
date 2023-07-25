// https://leetcode.com/problems/palindrome-number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        arr = self.numToArr(x)
        if(arr==arr[::-1]):
            return True
        return False
    def numToArr(self,num):
        arr = []
        if(num<0):
            arr.append('-')
        while(num>0):
            arr.append(str(num%10))
            num = num//10
        return arr