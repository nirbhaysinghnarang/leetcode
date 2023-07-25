// https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid]==target):
                return mid
            if(nums[mid]>target):
                right = mid-1
            else:
                left = mid+1
        return -1