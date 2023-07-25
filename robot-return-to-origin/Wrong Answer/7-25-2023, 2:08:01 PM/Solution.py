// https://leetcode.com/problems/robot-return-to-origin

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0,0]
        for mv in moves:
            if mv == "R":
                pos[1]+=1
            if mv == "U":
                pos[0]+=1
            if mv == "L":
                pos[1]-=1
            else:
                pos[0]-=1
        return pos[0] == 0 and pos[1]==0