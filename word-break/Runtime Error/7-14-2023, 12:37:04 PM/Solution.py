// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(index):
            if index==len(s):
                return True
            if index in memo:
                return index[memo]
            ans = False
            for word in wordDict:
                if s[index:].startswith(word):
                    ans = ans or dfs(index+len(word))
            memo[index]=ans
            return ans

           
            
        return dfs(0)