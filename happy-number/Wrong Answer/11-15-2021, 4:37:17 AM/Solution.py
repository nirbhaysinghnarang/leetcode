// https://leetcode.com/problems/happy-number

class Solution:
    prev = []
    def isHappy(self, n: int) -> bool:
        n = self.sum_squares(n)
        print(f'sum squares {n}')
        if (n==1):  return True
        if n in Solution.prev: 
            print(f'previously visited {n}')
            return False
        Solution.prev.append(n)
        return self.isHappy(n)
        
    def sum_squares(self, n):
        return sum([int(s)**2 for s in str(n)])