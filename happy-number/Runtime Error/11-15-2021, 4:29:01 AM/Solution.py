// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        n = self.sum_squares(n)
        if (n==1):  return True
        return self.isHappy(n)
        
    def sum_squares(self, n):
        return sum([int(s)**2 for s in str(n)])