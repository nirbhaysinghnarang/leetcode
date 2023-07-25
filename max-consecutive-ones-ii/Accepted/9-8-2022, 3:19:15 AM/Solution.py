// https://leetcode.com/problems/max-consecutive-ones-ii

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        num_zeroes_in_window = 0
        global_max = 0
        
        while(right<len(nums)):
            if nums[right]==0:
                num_zeroes_in_window+=1
            #stopping condition for exp.
            while(num_zeroes_in_window==2):
                #contract window here from the left
                #but before contracting, process left-most elem
                if(nums[left]==0):
                    #by process, reduce num of zeroes in window if left elem is 0
                    num_zeroes_in_window-=1
                left+=1
            global_max = max(global_max, right-left+1)
            #move right pointer forward
            right+=1
        return global_max
                