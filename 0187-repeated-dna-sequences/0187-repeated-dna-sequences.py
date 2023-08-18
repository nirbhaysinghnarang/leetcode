class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        ret = []
        L, R = 0, 9
        win_set = Counter()
        while R < len(s):
            subseq = s[L:R+1]
            win_set[subseq]+=1
            L+=1
            R+=1
        print(win_set)
        for s in win_set:
            if win_set[s] >1:
                ret.append(s)
        return ret
        