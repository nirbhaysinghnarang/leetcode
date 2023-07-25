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
            #iterate over first string
            #if letter key does not exist, create it.
           
            if not(s[idx] in dic):
                dic[s[idx]] = t[idx]
            else:
                # if letter is already in mapping, we see what it is mapped from
                if t[idx] in dic.values():
                    if {i for i in dic if dic[i]==t[idx]}!=s[idx]:
                        return False
                #if letter key exists, see what its prev mapping is.
                # if it is different, then return false,
                # if it is the same, do nothing?
                if dic[s[idx]]!=t[idx]:
                    return False
               
        return True
        