// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left_pointer = 0
        right_pointer = 0

        sz = 0

        while(right_pointer<len(s)):
            if not self.hasRepeatingChars(s[left_pointer:right_pointer]):
                right_pointer+=1
                sz = max(sz, right_pointer-left_pointer+1)
            else:
                left_pointer = right_pointer
    
        return sz



    def hasRepeatingChars(self,s):
        return list(set(s))==list(s)