class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hm = {
            "1":[],
            "2":['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }


        combinations = []

        def generateCombination(index, so_far):
            if index == len(digits):
                combinations.append(so_far)
                return

            letters = hm[digits[index]]
            for letter in letters:
                generateCombination(index+1, so_far+letter)


        generateCombination(0, "")
        return combinations