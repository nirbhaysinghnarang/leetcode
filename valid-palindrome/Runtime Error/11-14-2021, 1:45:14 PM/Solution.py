// https://leetcode.com/problems/valid-palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = clean(s)
        if len(s)<2:
            return True
        if(s[0]==s[-1]):
            return self.isPalindrome(s[1:-1])
        return False
            
        
    
    def clean(s):
        a = s.lower()
        a = "".join([char for char in s if char.isalnum()])
        return a
