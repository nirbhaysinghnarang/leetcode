class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        ret = []
        def r(i, cs):
            nonlocal ret, word
            if i == len(word):
                ret.append(cs)
            else:
                if not cs or not cs[-1].isdigit():
                    for j in range(i, len(word)):
                        r(j+1, cs + str(1 + j - i))
                r(i + 1, cs + word[i])
        r(0, "")
        return ret