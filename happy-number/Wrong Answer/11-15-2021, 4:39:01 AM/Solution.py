// https://leetcode.com/problems/happy-number

prev = []
class Solution:
    def isHappy(self, n: int) -> bool:
        global prev
        n = self.sum_squares(n)
        print(f'sum squares {n}')
        if (n==1):  return True
        if n in prev:
            print(f'previously visited {n}')
            return False
        prev.append(n)
        return self.isHappy(n)
        
    def sum_squares(self, n):
        return sum([int(s)**2 for s in str(n)])