// https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = ['a','e','i','o','u']
        
        vowels = [char for char in s if char in lst]
        
        vowels = vowels[::-1]
                
        vowelIdx = 0
        new = ""
        for (index, char) in enumerate(s):
            if char.lower() in lst:
                new+=(vowels[vowelIdx])
                vowelIdx+=1
            else:
                new+=char
            
        return new
                
                
                
            