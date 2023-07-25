// https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #non-opt
        c = 0
        pre = self.prefixSum(nums)
        for l in range(len(nums)):
            for r in range(l,len(nums)):
                if pre[r]-pre[l]==k:
                    c+=1
        return c




    def prefixSum(self, nums):
        pre = []
        tot = 0
        for n in nums:
            tot+=n
            pre.append(tot)
        return pre
        
    def query(self, pre, l, r):
        right = pre[r]
        left = pre[l-1] if l>0 else 0
        return right-left
