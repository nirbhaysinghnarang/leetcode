class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        win_set = set()
        L = 0
        mx = float('-inf')
        def _isSemiRep(i,j):
            numRep = sum(s[k] == s[k+1] for k in range(i,j))
            return numRep <=1
        for R in range(len(s)):
            while not _isSemiRep(L,R):
                L+=1
            mx = max(R-L+1, mx)
        return 0 if mx==float('-inf') else mx

