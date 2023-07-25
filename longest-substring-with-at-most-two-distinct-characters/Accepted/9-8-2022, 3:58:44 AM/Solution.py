// https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        #init left and right pointers
        left = 0
        right = 0
        #variable to keep track of global max
        global_max = 0
        #variable to keep track of distinct letters in window,
        #maps letters to their rightmost occurence
        dic = {}
        
        while(right<len(s)):
            #udpate right most or create if none exists
            dic[s[right]] = right
            #expand window
            right+=1
            #if stopping condition is reached, contract window
            # and process left most element
            # by process, remove the left most element from the dictionary
            # and then update left pointer
            while(len(dic)==3):
                to_delete = min(dic.values())
                del dic[s[to_delete]]
                left=to_delete+1
            
            global_max = max(global_max, right-left)
        return global_max
        