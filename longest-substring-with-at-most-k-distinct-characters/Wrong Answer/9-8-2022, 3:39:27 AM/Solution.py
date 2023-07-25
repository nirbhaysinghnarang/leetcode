// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        windowCharSet = set()
        left = 0
        right = 0
        global_max = 0
        
        while(right<len(s)):
            print("Left "+ str(left) + "Right " + str(right) +" Distinct Chars "+str(list(windowCharSet)))
            #process right element first
            if s[right] not in windowCharSet:
                windowCharSet.add(s[right])
            else:
                windowCharSet.remove(s[right])
            while(len(windowCharSet)==k+1):
                #process left element
                #then contract window
                if(s[left] not in windowCharSet):
                    windowCharSet.add(s[left])
                left+=1
            global_max = max(global_max, len(windowCharSet))
            right+=1
        return global_max
                