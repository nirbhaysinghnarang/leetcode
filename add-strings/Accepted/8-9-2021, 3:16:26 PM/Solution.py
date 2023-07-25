// https://leetcode.com/problems/add-strings

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if(num1=="0" and num2=="0"):
            return "0"
        num1 = self.stringToNum(num1)
        num2 = self.stringToNum(num2)
        res = num1+num2
        print(res)
        return self.numToString(res)
    def stringToNum(self, string):
        num = 0
        size = len(string)
        for i in range(0,size):
            num+=int(string[size-i-1])*(10**(i))
        return num
    def numToString(self,num):
        arr = []
        while(num>0):
            arr.append(str(num%10))
            num = num//10
        return "".join(arr[::-1])
            
        