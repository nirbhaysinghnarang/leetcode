// https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not len(s)%2:    return False
        dct = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for x in s:
            if x in dct.keys():
                stack.append(x)
            else:
                if not stack:   return False
                last = stack.pop()
                if last!=dct.get(x):    return False
        return stack==[]