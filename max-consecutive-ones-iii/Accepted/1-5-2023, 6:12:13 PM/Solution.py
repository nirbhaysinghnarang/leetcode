// https://leetcode.com/problems/max-consecutive-ones-iii

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        bits_flipped = 0
        left = 0
        global_maximum = 0
        for right in range(len(nums)):
            if nums[right]==0:
                bits_flipped += 1
            while bits_flipped > k and left < len(nums):
                if nums[left]==0: 
                    bits_flipped -=1
                left+=1
            global_maximum = max(global_maximum, right-left+1)
        return global_maximum





