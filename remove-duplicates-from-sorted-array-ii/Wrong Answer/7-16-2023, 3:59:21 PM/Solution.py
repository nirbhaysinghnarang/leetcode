// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 2,2

        while(R<len(nums)):
            if nums[R]==nums[R-1] and nums[R-2]==nums[R-1]:
                R+=1
                continue
            else:
                nums[L] = nums[R]
                L+=1
                R+=1
        return L