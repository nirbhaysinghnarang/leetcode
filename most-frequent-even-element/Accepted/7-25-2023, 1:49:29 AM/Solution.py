// https://leetcode.com/problems/most-frequent-even-element

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums = filter(lambda x: x%2==0, nums)
        if not nums:
            return -1

        c = Counter(nums)
        max_f = float('-inf')
        num = -1
        for key in c:
            if c[key] > max_f:
                max_f = c[key]
                num = key

            if c[key] == max_f:
                num = min(num, key)

        return num
