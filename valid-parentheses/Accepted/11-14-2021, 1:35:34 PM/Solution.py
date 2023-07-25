// https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2!=0:    return False
        dct = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for x in s:
            if x in dct.keys():
                stack.append(x)
            else:
                if not stack:   return False
                last = stack.pop()
                if x!=dct[last]:    return False
        return stack==[]