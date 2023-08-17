class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        sz = 0
        L = 0
        win_set = Counter()
        for R in range(len(s)):
            win_set[s[R]]+=1
            while len(win_set) > k:
                win_set[s[L]]-=1
                if win_set[s[L]]==0:
                    del win_set[s[L]]
                L+=1
            sz = max(R-L+1, sz)
        return sz