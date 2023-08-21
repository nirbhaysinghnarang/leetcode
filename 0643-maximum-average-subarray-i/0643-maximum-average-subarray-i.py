class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        L = 0
        s = 0
        for R in range(len(nums)):
            s+=nums[R]
            while L<R and R-L+1 > k:
                s-=nums[L]
                L+=1
            if R-L+1 == k:
                max_avg = max(max_avg, s/(R-L+1))
        return max_avg
