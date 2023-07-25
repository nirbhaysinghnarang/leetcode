// https://leetcode.com/problems/isomorphic-strings

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for idx in range(len(s)):
            if not(s[idx] in dic):
                dic[s[idx]] = t[idx]
            else:
                if dic[s[idx]]!=t[idx]:
                    return False
        return True
        