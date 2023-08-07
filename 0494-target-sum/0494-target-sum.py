class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(curr, nums):
            key = (curr, tuple(nums))
            if key in cache: return cache[key]
            if not nums: return 1 if curr == target else 0            
            res = dfs(curr - nums[0], nums[1:]) + dfs(curr + nums[0], nums[1:])
            cache[key] = res
            return res
        cache = {}        
        return dfs(0, nums)

 

