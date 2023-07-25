// https://leetcode.com/problems/isomorphic-strings

class Solution(object):
    
    def get_key(self, val, dic):
        for key, value in dic.items():
            if val == value:
                return key
        return -1

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic_s = {}
        dic_t = {}
        for idx in range(len(s)):
            if not(s[idx] in dic_s):
                dic_s[s_idx] = t_idx
            else:
                if dic_s[s_idx]!=t_idx:
                    return False
            if not (t[idx] in dic_t):
                dic_t[t_idx] = s_idx
            else:
                if dic_t[t_idx]!=s_idx:
                    return False
            
               
        return True
        