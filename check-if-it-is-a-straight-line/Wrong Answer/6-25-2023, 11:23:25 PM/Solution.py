// https://leetcode.com/problems/check-if-it-is-a-straight-line

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x = [l[0] for l in coordinates]
        y = [l[1] for l in coordinates]

        x = sorted(x)
        y = sorted(y)

        diff_x = x[1]-x[0]
        diff_y = y[1] - y[0]


        for i in range(2,len(x)-1):
            if x[i]-x[i-1]!=diff_x:
                return False
        
        for i in range(2,len(x)-1):
            if y[i]-y[i-1]!=diff_y:
                return False

        return True