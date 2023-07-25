// https://leetcode.com/problems/partition-to-k-equal-sum-subsets

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        W = sum(nums)
        sum_of_subset = W/len(nums)
        if not W%len(nums):
            return False

        cnt=0
        subsets = []

        def dfs(i, set1, tot):
            if i==len(nums) or tot==sum_of_subset:
                nonlocal cnt
                cnt+=1
                subsets.append(set1)
            

            thisnum = nums[i]
            is_there = False

            for set2 in subsets:
                if thisnum in set2:
                    is_there = True

            if not is_there:
                set1.append(thisnum)
                tot+=thisnum
                dfs(i+1, set1, tot)
                set1.pop()
                tot-=thisnum

        dfs(0, [], 0)
        return cnt==k
                
            


