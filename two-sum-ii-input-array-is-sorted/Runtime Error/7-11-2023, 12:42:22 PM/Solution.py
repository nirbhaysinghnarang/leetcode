// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    """
    Naive soln
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for (idx,i) in enumerate(numbers):
            comp=target-i
            if(comp<target):
                comp_idx = self.b_s(numbers, target, flag_idx)
            else:
                comp_idx = self.b_s_increasing(numbers, target, flag_idx)
            if(comp_idx!=-1):
                return [idx+1, comp_idx+1]
            
    
    def b_s(self, numbers, target, flag_idx):
        l, r = 0, len(numbers)-1
        while(l<=r):
            mid = (l+r)//2
            if numbers[mid]==target and mid!=flag_idx:
                return mid
            elif numbers[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return -1


    def b_s_increasing(self, numbers, target, flag_idx):
        l, r = 0, len(numbers)-1
        while(l<=r):
            mid = (l+r)//2
            if numbers[mid]==target and mid!=flag_idx:
                return mid
            elif numbers[mid]<target:
                r = mid-1
            else:
                l = mid+1
        return -1

    