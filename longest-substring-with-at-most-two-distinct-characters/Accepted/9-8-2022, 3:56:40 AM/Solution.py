// https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        global_max = 0
        dic = {}
        
        while(right<len(s)):
            dic[s[right]] = right
            right+=1
            
            while(len(dic)==3):
                to_delete = min(dic.values())
                del dic[s[to_delete]]
                left=to_delete+1
            
            global_max = max(global_max, right-left)
        return global_max
        