// https://leetcode.com/problems/find-in-mountain-array

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = self.getPeakIndex(mountain_arr)
        
        l_ans = self.searchLeft(mountain_arr[:peak])
        r_ans = self.searchRight(mountain_arr[peak+1:])

        if (mountain_arr[peak]==target):
            if(l_ans!=-1):
                return l_ans
            if(r_ans!=-1):
                return peak
            return r_ans
        return -1


    def searchLeft(self, l_half, target):
        l, r = 0, len(l_half)-1
        idx = -1
        while(l<=r):
            mid = (l+r)//2
            if(arr[mid]>=target):
                idx = mid
                right = mid-1
            else:
                left = mid+1
        return idx

    def searchRight(self, r_half, target):
        l, r = 0, len(l_half)-1
        idx = -1
        while(l<=r):
            mid = (l+r)//2
            if(arr[mid]<=target):
                idx = mid
                right = mid-1
            else:
                left = mid+1
        return idx


    def getPeakIndex(self, m_arr):
        l, r = 0, len(m_arr)-1
        peak = -1
        while(l<=r):
            mid = (l+r)//2
            if(mid==len(m_arr)-1 or m_arr[mid] >= m_arr[mid+1]):
                peak = mid
                right = mid-1
            else:
                left = mid+1
        return peak
