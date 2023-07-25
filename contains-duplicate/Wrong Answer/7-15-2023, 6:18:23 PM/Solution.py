// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        L, R = 0,0
        while(R<len(nums)):
            if nums[R]==nums[L] and L!=R:
                return True
            R+=1

        return False