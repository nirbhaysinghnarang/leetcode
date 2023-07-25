// https://leetcode.com/problems/kth-largest-element-in-an-array


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)
        return heapq.heappop(nums)