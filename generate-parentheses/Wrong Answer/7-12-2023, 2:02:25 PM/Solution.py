// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combs = []
        def gen(n, path, numstart, numend):
            if len(path)==2*n:
                combs.append("".join(path))
                return
            if numstart<n:
                gen(n, path+['('], numstart+1, numend)
            if numend<n:
                gen(n, path+[')'], numstart, numend+1)

        gen(n, [], 0, 0)
        return combs


            


