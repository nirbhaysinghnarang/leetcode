// https://leetcode.com/problems/container-with-most-water

class Solution(object):


    def maxArea(self, height):

        maxarea = 0
        l = 0
        r = len(height)-1

        while (l < r):
            maxarea = max(maxarea, min(height[l], height[r]) * (r-l))

            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1

        return maxarea