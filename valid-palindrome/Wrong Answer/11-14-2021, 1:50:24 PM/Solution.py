// https://leetcode.com/problems/valid-palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = self.clean(s)
        if len(a)<2:
            return True
        if(a[0]==a[-1]):
            return self.isPalindrome(a[1:-2])
        return False
            
        
    
    def clean(self,s):
        a = "".join([char for char in s if char.isalnum()])
        a = a.lower()
        return a
