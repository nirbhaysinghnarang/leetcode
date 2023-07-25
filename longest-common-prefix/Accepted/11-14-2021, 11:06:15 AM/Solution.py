// https://leetcode.com/problems/longest-common-prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        prefix = strs[0]
        if not prefix:
            return ''
        if(all([strs[i].startswith(prefix) for i in range(len(strs)) if i!=0])):
            return prefix
        return self.longestCommonPrefix([prefix[:-1]]+strs[1:])
                
            
            