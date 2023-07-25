// https://leetcode.com/problems/check-if-it-is-a-straight-line

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def get_m(p1,p2):
            try:
                return p2[1]-p1[1]/p2[0]-p1[0]
            except:
                return float('inf')

        m = get_m(coordinates[0],coordinates[1])
        for i in range(1, len(coordinates)-1):
            if(get_m(coordinates[i],coordinates[i+1])!=m):
                return False
        return True


    