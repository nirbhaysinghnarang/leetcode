// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]

        first = self.getFirstOccurence(nums,target)
        if first==-1:
            return [-1,-1]

        return [first, self.getLastOccurence(nums,target)]
        


    def getFirstOccurence(self, nums, target):
        l,r = 0, len(nums)-1
        ans = -1
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid]<target):
                l = mid+1
            else:
                ans = mid
                r = mid-1
        return ans

    def getLastOccurence(self, nums,target):
        l,r = 0, len(nums)-1
        ans = -1
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid]>target):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans-1
