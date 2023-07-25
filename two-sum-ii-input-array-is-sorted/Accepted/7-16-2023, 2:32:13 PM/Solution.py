// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
   
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers)-1
        while(L<R):
            s = numbers[L]+numbers[R]
            if s == target:
                return [L+1, R+1]
            if s < target:
                L += 1
            else: 
                R -= 1

        return [L+1, R+1]





        for (idx,i) in enumerate(numbers):
            comp=target-i
            if(comp<i):
                #must be to the left of current index
                left_subarray = numbers[:idx]
                comp_idx =  self.binarySearch(numbers[:idx], target, idx)
                if(comp_idx!=-1):
                    return [idx+1, comp_idx+1]
            else:
                #is to the rifh
                comp_idx = self.binarySearch(numbers[idx+1:], target, idx, False)
            if(comp_idx!=-1):
                return [idx+1, idx + 1+ comp_idx+1]
            
    
    def binarySearch(self, nums, target, flag):
        l, r = 0, len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid]==target and mid!=flag):
                return mid
            if nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return -1