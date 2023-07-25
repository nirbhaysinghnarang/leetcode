// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dic = {}

        for i in range(len(nums)-1):
            num = target-nums[i]
            sum_dic[num] = i
        print(sum_dic)
        for i in range(len(nums)-1):
            if(nums[i] in sum_dic):
                return [i,sum_dic[nums[i]]]
