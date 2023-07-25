// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
   
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for (idx,i) in enumerate(numbers):
            comp=target-i
            print(comp, i)
            if(comp<i):
                #must be to the left of current index
                left_subarray = numbers[:idx]
                comp_idx =  self.binarySearch(left_subarray, comp, idx)
                if(comp_idx!=-1):
                    return sorted([idx+1, comp_idx+1])
            else:
                #is to the right
                right_subarray = numbers[idx+1:]
                comp_idx = self.binarySearch(right_subarray, comp, idx)
                if(comp_idx!=-1):
                    return sorted([idx+1, comp_idx+1+idx+1])
            
    
    def binarySearch(self, nums, target, flag):
        l, r = 0, len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid]==target and mid!=flag):
                return mid
            if nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return -1