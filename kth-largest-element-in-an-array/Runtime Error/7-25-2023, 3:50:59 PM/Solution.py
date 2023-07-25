// https://leetcode.com/problems/kth-largest-element-in-an-array


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = heapq.heapify(nums)
        print(heap)
        for _ in range(k):
            heapq.heappop(heap)
        print(heap)
        return heapq.heappop(heap)