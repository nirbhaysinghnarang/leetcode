// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(index):
            if index==len(s):
                return 1
            if s[index]=='0':
                return 0
            if index in memo:
                return memo[index]
            cnt = 0
            cnt = dfs(index+1)
            if 10 <= int(s[index:index+2]) <= 26:
                cnt += dfs(index+2)
            memo[index]=cnt
            return cnt
            
            

        return dfs(0)
            



        