// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if(len(s)*k==0):
            return 0
        left = 0
        right = 0
        global_max = 1
        hashmap = {}
        while(right<len(s)):
            hashmap[s[right]] = right
            right+=1
            if(len(hashmap)==k+1):
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                left = del_idx+1
            global_max = max(global_max,right-left)
        return global_max
                