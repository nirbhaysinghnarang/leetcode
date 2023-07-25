// https://leetcode.com/problems/check-if-array-is-good

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = Counter()
        n = max(nums)
        for i in range(1,n+1):
            m[i]+=1
        m[n]+=1
        for num in nums:
            m[num] = max(0, m[num]-1)
        for key in m:
            if m[key]!=0:
                return False
        return True
            