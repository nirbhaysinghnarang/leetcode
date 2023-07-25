// https://leetcode.com/problems/find-pivot-index

class Solution(object):
    
    def sum_up_till_index(self,nums,index):
        return (sum(nums[:index]),sum(nums[index+1:]))
        
        
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for (i,num) in enumerate(nums):
            print(self.sum_up_till_index(nums,i))
            if(self.sum_up_till_index(nums,i)[0]==self.sum_up_till_index(nums,i)[1]):
                return i
        return -1
        
   