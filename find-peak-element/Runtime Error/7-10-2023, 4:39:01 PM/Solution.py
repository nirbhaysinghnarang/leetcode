// https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        #index of peak elt
        ans = -1
        #b-s loop
        while(l<=r):
            #middle elt 
            mid = (l+r)//2
            # elt is peak if it is greater than both neighbours
            if(arr[mid]>arr[mid+1]):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans
            
