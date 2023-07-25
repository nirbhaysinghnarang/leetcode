// https://leetcode.com/problems/longest-repeating-character-replacement

from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        maxSz = 0
        temp_k = k
        for R in range(1,len(s)):
            d = Counter(s[L:R+1])
            most_common = d.most_common(1)[1]
            print(d.most_common)
            winSize = R-L+1
            if winSize - most_common < temp_k:
                L += 1
                temp_k = k

            maxSz = max(maxSz, winSize)

        return maxSz


           

        return maxSz

                