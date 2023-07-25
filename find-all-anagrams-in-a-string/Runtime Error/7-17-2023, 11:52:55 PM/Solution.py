// https://leetcode.com/problems/find-all-anagrams-in-a-string

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = dict(Counter(p))
        L = 0
        window_dict = dict(Counter(s[:len(p)]))
        ans = [L] if window_dict == p_dict else []
        for R in range(p, len(s)):
            char = s[R]
            if char in window_dict:
                window_dict[char] += 1
            else:
                window_dict[char]=1

            window_dict[s[L]] = max(0, window_dict[s[L]]-1)
            if window_dict[s[L]]==0:
                del window_dict[s[L]]

            if p_dict == window_dict:
                ans.append(L)

            L+=1
        return ans


