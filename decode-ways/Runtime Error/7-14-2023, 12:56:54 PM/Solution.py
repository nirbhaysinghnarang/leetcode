// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:

        def dfs(index):
            try:
                if s[index-1]=='0':
                    return 0
            except:
                if index==len(s)-1:
                    if int(s[index])>0 and int(s[index])<27:
                        return 1
                    return 0

                ans = 1 if int(s[index])>0 and int(s[index])<27 else 0
                ans = ans + dfs(index+1)
                return ans

        return dfs(0)
            



        