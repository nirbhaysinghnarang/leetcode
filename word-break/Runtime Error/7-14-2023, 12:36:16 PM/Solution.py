// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(index):

            if index==len(s):
                return True
            ans = False
            for word in wordDict:
                if s[index:].startsWith(word):
                    ans = ans or dfs(index+len(word))
            return ans

           
            
        return dfs(0)