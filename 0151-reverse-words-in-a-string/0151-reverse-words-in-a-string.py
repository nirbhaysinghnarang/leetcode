class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        L,R = 0, len(words)-1
        new_words = ["" for _ in range(len(words))]
        while(L<=R):
            new_words[L] = words[R]
            new_words[R] = words[L]
            R-=1
            L+=1
        clean = []
        for word in new_words:
            if word!="" and word!=' ':
                clean.append(word)
        return " ".join(clean)