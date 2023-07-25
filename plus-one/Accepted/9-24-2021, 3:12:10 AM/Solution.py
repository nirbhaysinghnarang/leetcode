// https://leetcode.com/problems/plus-one

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        numRepr = self.getNum(digits)
        numRepr+=1
        print(numRepr)
        return self.getArrRepr(numRepr)
        
    def getNum(self,digits):
        num = 0
        max_power_of_ten = len(digits)-1
        for i in range(0,len(digits)):
            num+=digits[len(digits)-1-i]*(10**i)
        return num
    
    def getNumDigs(self,num):
        return len(str(num))
    
    def getArrRepr(self,num):
        numDigits = self.getNumDigs(num)
        numArr = [0 for x in range(numDigits)]
        index = numDigits-1
        while(num>0):
            numArr[index] = num%10
            num = num//10
            index-=1
        return numArr
                
        