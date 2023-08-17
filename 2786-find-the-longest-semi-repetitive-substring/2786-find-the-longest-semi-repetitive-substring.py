class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        win_set = set()
        L = 0
        mx = float('-inf')
        def _isSemiRep(string):
            cnt = 0
            for (i, char) in enumerate(string):
                for (j,char1) in enumerate(string):
                    if abs(i-j)==1 and char==char1:
                        cnt+=1
            return cnt<=2
        for R in range(len(s)):
            string = s[L:R+1]
            while not _isSemiRep(string):
                L+=1
                string = s[L:R+1]
            print(string)
            mx = max(R-L+1, mx)
        return 0 if mx==float('-inf') else mx

