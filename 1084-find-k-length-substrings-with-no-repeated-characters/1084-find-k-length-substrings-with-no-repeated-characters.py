class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        win_set = set()
        L = 0
        num = 0
        if k > len(s):
            return 0

        for R in range(len(s)):
            new_char = s[R]
            while new_char in win_set:
                old_char = s[L]
                win_set.remove(old_char)
                L+=1
            win_set.add(new_char)
            if R-L+1 >= k:
                num+=1

        return num

