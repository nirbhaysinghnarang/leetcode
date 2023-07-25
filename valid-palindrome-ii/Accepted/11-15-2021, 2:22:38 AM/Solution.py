// https://leetcode.com/problems/valid-palindrome-ii

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s)-1
        while(l<r):
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return self.isPalin(s[l:r]) or self.isPalin(s[l+1:r+1])
        return True
    
    def isPalin(self,s):
        return s==s[::-1]