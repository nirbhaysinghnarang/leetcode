// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<3:
            return nums

        L, R = 0,0

        while(R<len(nums)):
            count = 1
            while(R+1 < len(nums) and nums[R]==nums[R+1]):
                count+=1


            for i in range(min(2, count)):
                nums[L]=nums[R]
                L+=1

            R+=1

        return L