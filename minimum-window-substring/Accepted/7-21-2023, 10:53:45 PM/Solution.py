// https://leetcode.com/problems/minimum-window-substring

from collections import Counter

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        target_counter = Counter(t)
        required_chars = len(target_counter)
        L, R = 0, 0
        min_ss = ""
        min_ss_cnt = float('inf')

        while R < len(s):
            if s[R] in target_counter:
                target_counter[s[R]] -= 1
                if target_counter[s[R]] == 0:
                    required_chars -= 1

            while required_chars == 0:
                if R - L + 1 < min_ss_cnt:
                    min_ss_cnt = R - L + 1
                    min_ss = s[L:R+1]

                if s[L] in target_counter:
                    target_counter[s[L]] += 1
                    if target_counter[s[L]] > 0:
                        required_chars += 1

                L += 1

            R += 1

        return min_ss
