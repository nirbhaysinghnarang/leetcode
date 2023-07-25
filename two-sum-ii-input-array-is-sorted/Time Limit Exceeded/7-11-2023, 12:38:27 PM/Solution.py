// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for (idx,i) in enumerate(numbers):
            comp = target-i
            comp_idx = self.b_s(numbers, comp)
            if(comp_idx!=-1):
                return [idx+1, comp_idx+1]


    def b_s(self, numbers, target):
        l, r = 0, len(numbers)-1
        while(l<=r):
            mid = (l+r)//2
            if numbers[mid]==target:
                return mid
            elif numbers[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return -1