// https://leetcode.com/problems/partition-to-k-equal-sum-subsets

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        W = sum(nums)
        sum_of_subset = W/k
        print(W, sum_of_subset)
        if not W%k:
            return False

        subsets = []

        def dfs(i, p, tot):
            if tot==sum_of_subset:
                subsets.append(p.copy())

            for x in range(i, len(nums)):
                if tot+nums[x] > sum_of_subset:
                    continue
                
                p.append(nums[x])
                tot+=nums[x]
                dfs(x+1, p, tot)
                p.pop()
                tot-=nums[x]

        dfs(0, [], 0)
        print(subsets)
            


