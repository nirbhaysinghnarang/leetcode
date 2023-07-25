// https://leetcode.com/problems/find-the-duplicate-number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f, s = 0,0

        while(f < len(nums)):
            f+=2
            s+=1

            if nums[s] == nums[f]:
                return nums[s]

        

        