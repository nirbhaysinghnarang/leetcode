// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dic = {}
        for i in range(len(nums)-1):
            sum_dic[i] = target-nums[i]
        for i in sum_dic:
            if(sum_dic[i] in nums):
                return (i,sum_dic[i])

        