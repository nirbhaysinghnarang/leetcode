// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #step 1 - create a set
        charSet = set()
        #create the return variable
        res = 0
        # create left pointer to 0
        l = 0
        #iterate over string
        for r in range(len(s)):
            # while the character is a duplicate, smallen the sliding window
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res
                
            
        