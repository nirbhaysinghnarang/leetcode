// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        maxSz = 0
        L = 0
        for R in range(len(s)):
            curString = s[L:R]
            while not curString == curString[::-1]:
                L+=1
            
            if R-L+1>maxSz:
                maxSz = R-L+1
                ans = s[L:R]

        return ans
            



