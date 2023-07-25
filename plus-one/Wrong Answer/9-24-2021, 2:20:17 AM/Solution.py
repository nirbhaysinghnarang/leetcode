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
        return self.getArr(numRepr,numDigs)
        
        
    def getNum(self,digits):
        num = 0
        max_power_of_ten = len(digits)-1
        for i in range(0,len(digits)):
            num+=digits[len(digits)-1-i]*(10**i)
        return num

    def getArr(self,num,numDigs):
        arr = [0 for i in range(numDigs)]
        tmp = num
        counter = numDigs-1
        while tmp>0:
            arr[counter] = tmp%10
            tmp = tmp//10
            counter-=1
        return arr