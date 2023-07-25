// https://leetcode.com/problems/arithmetic-subarrays

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for i in range(len(l)):
            answer.append(self.isArithmetic(nums[l[i]:r[i]]))
        return answer


    def isArithmetic(self, lst):
        lst = sorted(lst)

        diff = lst[0]-lst[1]

        for(i in range(len(lst))):
            if(lst[i]-lst[i+1])!=diff:
                return False
        return True