// https://leetcode.com/problems/top-k-frequent-elements

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return Counter(nums).most_common(k)