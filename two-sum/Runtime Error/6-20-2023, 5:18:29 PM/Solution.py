// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dic = {}
        for i in range(len(nums)-1):
            elem = target-nums[i]
            sum_dic[elem] = i
        for i in range(len(nums)-1):
            if(nums[i] in sum_dic):
                return (sum_dic[i],i)
            
        