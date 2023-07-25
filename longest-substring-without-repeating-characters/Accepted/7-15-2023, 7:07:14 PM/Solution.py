// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        window_set = set()
        maxcnt = 0
        

        for R in range(len(s)):

            while s[R] in window_set:
                window_set.remove(s[L])
                L+=1
            window_set.add(s[R])
            maxcnt = max(maxcnt, len(window_set))

        return maxcnt

            
