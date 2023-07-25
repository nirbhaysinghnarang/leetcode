// https://leetcode.com/problems/minimum-window-substring

from collections import Counter
class Solution:

    def isIncl(self, hm,t):
        print(hm, t)
        for char in t:
            if not char in hm:
                return False
            else:
                if hm[char]==1:
                    del hm[char]
                else:
                    hm[char]-=1
        return True

    def minWindow(self, s: str, t: str) -> str:

        L = 0
        t_counter = Counter(t)
        window_counter = Counter()
        min_ss = ""
        min_ss_cnt = float('inf')

        for R in range(len(s)):
            print(s[L:R])
            #update counter
            window_counter[s[R]]+=1
            #shrink window while condition is met
            while self.isIncl(window_counter, t):
                print(s[L:R]+"HELLO")
                if R-L+1 < min_ss_cnt:
                    string = s[L:R]
                    min_ss_cnt = R-L+1
                    min_ss = string
                window_counter[s[L]]-=1
                if window_counter[s[L]]==0:
                    del window_counter[s[L]]
                L-=1


        return min_ss




        