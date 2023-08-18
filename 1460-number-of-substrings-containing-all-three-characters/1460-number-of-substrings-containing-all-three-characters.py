class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        win_set = Counter()
        L = 0
        num_strings = 0

        for R in range(len(s)):
            win_set[s[R]]+=1
            while win_set['a'] > 0 and win_set['b']>0 and win_set['c'] > 0:
                win_set[s[L]]-=1
                L+=1
            num_strings+=L


        return num_strings

        