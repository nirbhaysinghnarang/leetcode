// https://leetcode.com/problems/majority-element-ii

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj = []
        counter = Counter(nums)
        for key in counter:
            if counter[key] > len(nums)//3:
                maj.append(key)

        return maj

