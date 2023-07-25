// https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #define bounds of current window
        left = 0
        right = 0
        #keep track of window with max ones so far
        ans = 0
        #num of ones in current window
        nums_ones = 0

        for idx in range(1,len(nums)):
            if nums[idx]==1:
                right+=1   
                nums_ones+=1
                if(nums_ones>ans):
                    ans = nums_ones
            else:
                #break window
                left = idx
                right = idx
                nums_ones = 0
        return ans



        