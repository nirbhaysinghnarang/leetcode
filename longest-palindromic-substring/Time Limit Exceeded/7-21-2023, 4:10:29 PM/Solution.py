// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        maxSz = 0
        for L in range(len(s)):
            for R in range(L + 1, len(s) + 1):  # Adjust R range to cover all substrings
                curString = s[L:R]
                if curString == curString[::-1]:
                    # Update answer if a longer palindrome is found
                    if R - L > maxSz:
                        maxSz = R - L
                        ans = curString
        return ans

            



