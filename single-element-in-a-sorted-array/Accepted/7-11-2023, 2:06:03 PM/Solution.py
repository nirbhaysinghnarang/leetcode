// https://leetcode.com/problems/single-element-in-a-sorted-array

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Intuition:
        we know an element appears only once if it is different than both its neighbours
        so we binary search using the following magix
        """
        if len(nums)==1:
            return nums[0]
        l, r = 0, len(nums)-1
        sz = len(nums)
        while(l<=r):
            mid = (l+r)//2
            elt = nums[mid]
            if mid!=0 and mid!=sz-1:
                if elt!=nums[mid-1] and elt!=nums[mid+1]:
                    return elt
                #now elt[mid] must either equal elt[mid+1] or elt[mid-1]
                if(nums[mid]==nums[mid+1]):
                    left_half = nums[:mid]
                    right_half=nums[mid+2:]
                    if(len(left_half)%2!=0):
                        #answer is in left half
                        r = mid-1
                    else:
                        #answer is in right half
                        l = mid+1
                else:
                    left_half = nums[:mid-1]
                    right_half = nums[mid+1:]
                    if(len(left_half)%2!=0):
                        #answer is in left half
                        r = mid-1
                    else:
                        #answer is in right half
                        l = mid+1
            if mid==0 or mid==sz-1:
                return elt

                