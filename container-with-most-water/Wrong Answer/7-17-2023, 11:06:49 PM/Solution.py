// https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_end = 0
        right_end = len(height)-1

        max_vol = 0
        while(left_end < right_end):
            left_height = height[left_end]
            right_height = height[right_end]
            max_vol = max(max_vol, min(left_height, right_height) * right_end - left_end)
            if left_height < right_height:
                left_end+=1
            else:
                right_end-=1

        return max_vol
