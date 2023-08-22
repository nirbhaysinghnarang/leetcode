class Solution:
    def tribonacci(self, n: int) -> int:
        
        def topDown(n):
            if n<=0:
                return 0
            if n<=2:
                return 1
            return topDown(n-1)+topDown(n-2)+topDown(n-3)
        memo = {}
        def topDownWithMemo(n):
            if n in memo:
                return memo[n]
            if n<=0:
                return 0
            if n<=2:
                return 1
            ans = topDown(n-1)+topDown(n-2)+topDown(n-3)
            memo[n] = ans
            return ans
        
        def bottomUp(n):
            if n<=0:
                return 0
            if n<=2:
                return 1
            dp = [-1 for _ in range(n+1)]
            dp[0] = 0
            dp[1]=1
            dp[2] = 1
            for i in range(3,n+1):
                dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
            return dp[n]
        return bottomUp(n)
    
    