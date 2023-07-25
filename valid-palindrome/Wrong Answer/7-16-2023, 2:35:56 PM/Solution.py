// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s)-1
        while(L<R):
            if s[L].lower()!=s[R].lower() and (s[L].isalnum() and s[R].isalnum()):
                return False

            else:
                L+=1
                R-=1

        return True