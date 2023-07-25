// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hm = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        soln = []

        def dfs(index, p):
            if index==len(digits):
                soln.append("".join(p))
                return

            letters = hm[digits[index]]
            for letter in letters:
                p.append(letter)
                dfs(index+1, p)
                p.pop()

        dfs(0,[])
        return soln

