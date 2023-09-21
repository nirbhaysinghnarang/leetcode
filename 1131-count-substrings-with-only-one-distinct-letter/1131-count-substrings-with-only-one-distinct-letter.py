class Solution:
    def countLetters(self, s: str) -> int:
        ans, left, C = 0, 0, Counter()
        for right in range(len(s)):
            C[s[right]] += 1
            while len(C) > 1:
                left +=1
                C = Counter(s[left:right+1])
            ans += (right - left + 1)
        return ans
        