// https://leetcode.com/problems/happy-number

class Solution:
    prev = []
    def isHappy(self, n: int) -> bool:
        Solution.prev.append(n)
        n = self.sum_squares(n)
        if (n==1):  return True
        if n in Solution.prev:   return False
        return self.isHappy(n)
        
    def sum_squares(self, n):
        return sum([int(s)**2 for s in str(n)])