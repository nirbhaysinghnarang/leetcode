class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxSz = 0

        # for every character in the string, consider it to be the center of an expanding 
        # palidrome

        for i in range(len(s)):
            #odd length
            L, R = i, i
            while L >=0 and R<len(s) and s[L] == s[R]:
                if R-L+1 > maxSz:
                    maxSz = R-L+1
                    res = s[L:R+1]
                L-=1
                R+=1
            # even length
            L, R = i, i+1
            while L >=0 and R<len(s) and s[L] == s[R]:
                if R-L+1 > maxSz:
                    maxSz = R-L+1
                    res = s[L:R+1]
                L-=1
                R+=1

        return res


            



