// https://leetcode.com/problems/nth-digit

class Solution:
    def findNthDigit(self, n: int) -> int:
        nums = [str(i+1) for i in range(n)]
        str_nums = "".join(nums)
        return str_nums[n-1]