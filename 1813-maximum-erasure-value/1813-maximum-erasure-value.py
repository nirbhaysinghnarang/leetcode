class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_sum = 0
        win_set = set()
        win_sum = 0
        L = 0
        for R in range(len(nums)):
            while nums[R] in win_set:
                win_set.remove(nums[L])
                win_sum -= nums[L]
                L+=1
            win_set.add(nums[R])
            win_sum += nums[R]
            max_sum = max(win_sum, max_sum)
        return max_sum