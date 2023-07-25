// https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        ans = len(arr)
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                r = mid-1
                ans = mid
            else:
                l=mid+1
        return ans