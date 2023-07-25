// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dic = {}
        for i in range(len(nums)):
            num = target - nums[i]
            sum_dic[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in sum_dic and sum_dic[complement] != i:
                return [i, sum_dic[complement]]
