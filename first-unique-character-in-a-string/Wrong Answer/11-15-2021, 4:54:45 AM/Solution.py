// https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        if s[0] in s[1:]:
            print('yes')
            return self.firstUniqChar(s[1:])
        return 0
        