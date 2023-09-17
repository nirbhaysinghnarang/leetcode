class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        abbrvs = []
        def generateAbbr(index, abbr):
            if index >= len(word):
                abbrvs.append(abbr)
                return
            if not abbr or not str(abbr[-1]).isdigit():
                for end in range(index, len(word)):
                    generateAbbr(end+1, abbr+str(end-index+1))
            generateAbbr(index+1, abbr+word[index])
        generateAbbr(0,"")
        return abbrvs
        

            