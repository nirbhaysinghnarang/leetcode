// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = -1
        l, r = 0, len(nums)-1
        pivot = nums[0]
        while(l<=r):
            mid = (l+r)//2
            if (arr[mid]>=pivot):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans