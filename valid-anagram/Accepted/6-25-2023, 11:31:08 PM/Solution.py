// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for char in s:
            if dic.get(char):
                dic[char]+=1
            else:
                dic[char]=1
        
        for char in t:
            if not dic.get(char):
                return False
            else:
                dic[char]-=1

        for key in dic:
            if dic[key]!=0:
                return False

        return True
