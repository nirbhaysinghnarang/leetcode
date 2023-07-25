// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums)==1:
            return nums[0]


        left = nums[:len(nums)//2]
        right = nums[len(nums)//2:]
        return self.majorityElement(left) or self.majorityElement(right)
             


        
