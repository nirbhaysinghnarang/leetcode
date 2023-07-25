// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_end = []
        right_end = []


        l_tot = 1
        for i in range(len(nums)):
            left_end.append(l_tot)
            l_tot *= nums[i]

        r_tot = 1
        rev_nums = nums[::-1]
        for i in range(len(rev_nums)):
            right_end.append(r_tot)
            r_tot *= rev_nums[i]

        right_end = right_end[::-1]

        ans = []
        for i in range(len(right_end)):
            ans.append(right_end[i]*left_end[i])

        return ans
        