// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Intuition:
        Rotated sorted array has two sorted arrays.
        Minimum elt is the first element of the second sorted array
        Largest element of second sorted array is the last element
        This element is smaller than all elements in the first sorted array but
        larger than all elements in the next sorted array

        """
        max_of_second = nums[-1]
        l, r = 0, len(nums)-1
        boundary_index = -1
        while(l<=r):
            mid = (l+r)//2
            if (nums[mid]<max_of_second):
                r = mid-1
                boundary_index = mid
            else:
                l = mid+1
        return nums[boundary_index]