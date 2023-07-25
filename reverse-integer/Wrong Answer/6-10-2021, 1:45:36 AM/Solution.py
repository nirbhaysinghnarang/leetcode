// https://leetcode.com/problems/reverse-integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if(x<0):
            neg = True
            x=x*(-1)
        digs = []
        while(x>0):
            digs.append(x%10)
            x=x//10
        ret = 0
        index = 1
        print(digs)
        for dig in digs:
            ret += dig*(10**(len(digs)-index))
            index+=1
        if(neg):
            ret*=-1
        return ret
    
    
        
        