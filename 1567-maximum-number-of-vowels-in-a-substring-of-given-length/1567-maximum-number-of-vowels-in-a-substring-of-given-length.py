class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count = 0
        win_vowel_count = 0
        L=0
        for R in range(len(s)):
            new_char = s[R]
            if new_char in ['a','e','i','o','u']:
                win_vowel_count+=1
            while R-L+1 > k:
                old_char = s[L]
                if old_char in ['a','e','i','o','u']:
                    win_vowel_count-=1
                L+=1
            max_count = max(win_vowel_count, max_count)

        return max_count


        

