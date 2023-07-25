// https://leetcode.com/problems/find-the-highest-altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [0]
        s = 0

        for i in range(len(gain)):
            s+=gain[i]
            arr.append(s)

        return max(arr)