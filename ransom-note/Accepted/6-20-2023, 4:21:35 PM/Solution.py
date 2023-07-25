// https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for char in magazine:
            if char in dic:
                dic[char]+=1
            else:
                dic[char]=1

        for char in ransomNote:
            if dic.get(char) is None or dic[char]<1:
                return False
            else:
                dic[char]-=1
            
        return True