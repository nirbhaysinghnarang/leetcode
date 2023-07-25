// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        max_of_second_half = nums[-1]

        l, r = 0, len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid]>max_of_second_half:
                l = mid+1
            else:
                r = mid-1

        return l