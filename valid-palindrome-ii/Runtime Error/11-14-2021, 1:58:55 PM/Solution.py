// https://leetcode.com/problems/valid-palindrome-ii

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        while(left<right):
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return s[l:r]==s[l:r][::-1] or s[l+1:r+1]==s[l+1:r+1][::-1]
            return True