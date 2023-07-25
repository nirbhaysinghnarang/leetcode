// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            for char2 in t:
                try:
                    if(char==char2):
                        t = t.replace(char2, "")
                except:
                    return False
        return True
        