// https://leetcode.com/problems/find-pivot-index

class Solution(object):
    
    def get_prefix_sum(self,nums):
        prefix_sum = [0 for i in range(len(nums))]
        prefix_sum[0] = nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1]+nums[i]
        return prefix_sum
        
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = self.get_prefix_sum(nums)
        print(prefix_sum)
        for i in range(len(nums)):
            l_sum = prefix_sum[i]-nums[i]
            r_sum = prefix_sum[-1]-prefix_sum[i]
            print("for index {}, l_sum{}, r_sum{}".format(i,l_sum,r_sum))
            if(l_sum==r_sum):
                return i
        return -1
        
   