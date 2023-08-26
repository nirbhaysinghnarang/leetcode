class Solution:
    def jump(self, nums: List[int]) -> int:
        #dp[i]: min num of jumps to go from i to n-1
        #for i in range(n-2, -1, -1)
            #dp[i] = min(for n in nums[i]: n + dp[i+n])

        #base case: dp[n-1] = 0
        #return dp[0]
        n = len(nums)
        dp = [float('inf') for _ in range(n)]
        dp[n-1] = 0


        for i in range(n-2, -1,-1):
            available_steps = nums[i]
            for j in range(i+1, min(n-1, i+nums[i])+1):
                dp[i] = min(dp[i], dp[j])
            if dp[i]!=float('inf'):
                dp[i]+=1

        return dp[0]


            
            
            
            
            
        return dp[0]
