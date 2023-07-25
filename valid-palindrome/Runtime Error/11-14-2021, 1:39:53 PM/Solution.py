// https://leetcode.com/problems/valid-palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = "".join([char for char in s if char.isalnum()])
        if len(s)<2:
            return True
        if(s[0]==s[-1]):
            return self.isPalindrome(self, s[1:-2])
        return False
            
        
    
        