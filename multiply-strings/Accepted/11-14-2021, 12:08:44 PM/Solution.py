// https://leetcode.com/problems/multiply-strings

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = int(num1)
        num2 = int(num2)
        return str(num1*num2)