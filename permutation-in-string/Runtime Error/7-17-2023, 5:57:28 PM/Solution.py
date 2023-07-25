// https://leetcode.com/problems/permutation-in-string

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq_dic = dict(Counter(s1))
        window_size =len(s1)
        L = 0
        R_INIT = window_size-1
        window_dic = dict(Counter(s2[:R_INIT+1]))
        for R in range(R_INIT, len(s2)):
            if s2[R] in window_dic:
                window_dic[s2[R]]+=1
            else:
                window_dic[s2[R]]=1

            if window_dic==s1_freq_dic:
                return True

            window_dic[s2[L]] = max(0, window_dic[s2[L]-1])
            L+=1

        return False

            
            
        return False

