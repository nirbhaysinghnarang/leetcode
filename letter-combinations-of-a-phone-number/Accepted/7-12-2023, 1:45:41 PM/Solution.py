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
        combs = []
        def dfs(idx, path):
            if idx==len(digits):
                combs.append("".join(path))
            else:
                letters = hm.get(digits[idx])
                for l in letters:
                    dfs(idx+1, path+[l])
        
        dfs(0, [])
        return combs