// https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        temp_k = k

        maxSz = 0
        winSize = 0

        for R in range(1,len(s)):
            print(s[R], temp_k)
            if s[R]==s[L]:
                winSize+=1
            elif (s[R]!=s[L] and temp_k>0):
                winSize+=1
                temp_k-=1
            elif k==0:
                L = R
                temp_k = k
                winSize=0

            maxSz = max(winSize, maxSz)

        return maxSz

                