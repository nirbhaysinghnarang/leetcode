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
        mapST = {}
        mapTS = {}
        for (c1, c2) in zip(s,t):
            if ((c1 in mapST and mapST[c1]!=c2) or (c2 in mapTS and mapTS[c2]!=c1)):
                return False
            mapST[c1]=c2
            mapTS[c2]=c1
            
               
        return True
        