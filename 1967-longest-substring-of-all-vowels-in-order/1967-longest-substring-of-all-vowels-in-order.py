class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        L = 0
        maxLen = 0
        sz = 0
        prev = 'a'
        win_set = set()
        for R in range(len(word)):
            newChar = word[R]
            if newChar >= prev:
                sz+=1
                win_set.add(newChar)
            else:
                win_set = {newChar}
                sz=1
            prev = newChar
            if len(win_set) == 5:
                maxLen = max(sz, maxLen)
        return maxLen