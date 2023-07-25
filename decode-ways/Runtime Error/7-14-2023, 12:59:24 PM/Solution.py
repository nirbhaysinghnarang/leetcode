// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        def getPos(char):
            return string.ascii_lowercase.index(char.lower())+1

        def dfs(index):
            
            if index==len(s)-1:
                if int(s[index])>0 and int(s[index])<27:
                    return 1
                return 0
            if s[index]=='0':
                return 0
            ans = 1 if ints[index])>0 and s[index]<27 else 0
            ans = ans + dfs(index+1)
            return ans

        return dfs(0)
            



        