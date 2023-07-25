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
        dic = {}
        for idx in range(len(s)):
            #iterate over first string
            #if letter key does not exist, create it.
            if not(s[idx] in dic):
                dic[s[idx]] = t[idx]
            else:              
                #if letter key exists, see what its prev mapping is.
                # if it is different, then return false,
                # if it is the same, do nothing?
                if(t[idx] in dic.values()):
                    #if letter has already been mapped to
                    #see what mapped to it
                    mapped_from = self.get_key(t[idx], dic)
                    print(mapped_from)
                    if mapped_from != t[idx]:
                        return False
                if dic[s[idx]]!=t[idx]:
                    return False
               
        return True
        