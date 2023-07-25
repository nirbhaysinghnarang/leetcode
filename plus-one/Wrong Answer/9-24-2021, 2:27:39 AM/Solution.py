// https://leetcode.com/problems/plus-one

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        numRepr = self.getNum(digits)
        numDigs = len(digits)
        print(numRepr)
        numRepr+=1
        return self.getArr(numRepr)
    def getNum(self,digits):
        num = 0
        max_power_of_ten = len(digits)-1
        for i in range(0,len(digits)):
            num+=digits[len(digits)-1-i]*(10**i)
        return num
    def getArr(self,num):
        numDigs = self.getNumDigs(num)
        arr = [0 for i in range(numDigs)]
        tmp = num
        counter = numDigs-1
        while tmp>0:
            arr[counter] = tmp%10
            tmp = tmp//10
            counter-=1
        return arr
    def getNumDigs(self,num):
        if(num<10):
            return 1
        if(num>=10):
            return 2
        numDigs = 0
        tmp = num
        while(tmp>0):
            tmp = tmp//10
            numDigs+=1
        return numDigs