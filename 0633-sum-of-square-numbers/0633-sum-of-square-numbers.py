class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        L = 0
        R = int(c**(1/2))

        while L<=R:
            res = L**2 + R**2
            if res == c:
                return True
            if res > c:
                R-=1
            else:
                L+=1
        return False