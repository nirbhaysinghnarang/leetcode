// https://leetcode.com/problems/happy-number

class Solution:
    prev = []
    def isHappy(self, n: int) -> bool:
        return self.solve(n, [])
    
    def solve(self, n, prev):
        n = self.sum_squares(n)
        if (n==1):  return True
        if n in prev:
            return False
        prev.append(n)
        return self.solve(n, prev)
        
        
    def sum_squares(self, n):
        return sum([int(s)**2 for s in str(n)])