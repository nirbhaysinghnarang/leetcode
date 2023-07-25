// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
   
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for (idx,i) in enumerate(numbers):
            comp=target-i
            if(comp<target):
                comp_idx = self.binarySearch(numbers, target, idx, True)
            else:
                comp_idx = self.binarySearch(numbers, target, False)
            if(comp_idx!=-1):
                return [idx+1, comp_idx+1]
            
    
    def binarySearch(self, nums, target, flag, isIncreasing):
        l, r = 0, len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid]==target):
                return mid
            if (isIncreasing):
                if(nums[mid]>target):
                    right = mid-1
                else:
                    left = mid+1
            else:
                if(nums[mid]>target):
                    left = mid+1
                else:
                    right = mid -1
        return -1