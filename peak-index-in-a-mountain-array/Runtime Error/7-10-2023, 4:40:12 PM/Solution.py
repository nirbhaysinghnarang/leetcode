// https://leetcode.com/problems/peak-index-in-a-mountain-array

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        arr = nums
        l, r = 0, len(nums)-1
        #index of peak elt
        ans = -1
        #b-s loop
        while(l<=r):
            #middle elt 
            mid = (l+r)//2
            # elt is peak if it is greater than both neighbours
            if(mid==len(arr)-1 or arr[mid]>arr[mid+1]):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans