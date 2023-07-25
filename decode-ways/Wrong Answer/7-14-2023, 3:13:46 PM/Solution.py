// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:

        def dfs(index):
            if index==len(s):
                return 1
            
            if s[index]=='0':
                return 0
            else:
                cnt = 1
            for i in range(index+1, len(s)):
                if int(s[index:i+1])>0 and int(s[index:i+1])<27:
                    cnt = 1 + dfs(i)
                else:
                    cnt = dfs(i)
            return cnt
            

        return dfs(0)
            



        