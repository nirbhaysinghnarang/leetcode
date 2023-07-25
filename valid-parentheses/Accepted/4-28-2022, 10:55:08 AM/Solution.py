// https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #case 1: len(s)<2
        if(len(s)<2):
            return False
        #case 2: odd no. of chars
        if (len(s)%2):
            return False
        paren_dic = {
            "{":"}",
            "(":")",
            "[":"]"
        }
        stack = []
        for char in s:
            if char in paren_dic.keys():
                stack.append(char)
            else:
                if len(stack)==0 or char!=paren_dic[stack.pop()]:
                    return False
        return stack==[]