// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]

        mid = len(nums)//2

        left = nums[:mid]
        right = nums[mid:]

        majLeft = self.majorityElement(left)
        numEqualsLeftCheck = 0

        for elem in right:
            if elem == majLeft:
                numEqualsLeftCheck+=1

        if numEqualsLeftCheck >= len(right)//2:
            return majLeft

        majRight = self.majorityElement(right)

        numEqualsRightCheck = 0
        for elem in left:
            if elem == majRight:
                numEqualsRightCheck+=1

        if numEqualsRightCheck >= len(left)//2:
            return majRight


