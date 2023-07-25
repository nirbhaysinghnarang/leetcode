// https://leetcode.com/problems/length-of-last-word

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        s = s.split(" ")
        return len(s[-1])
        