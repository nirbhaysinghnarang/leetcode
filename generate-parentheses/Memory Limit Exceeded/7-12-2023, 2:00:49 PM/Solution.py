// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combs = []
        def gen(n, path, numstart, numend):
            if numstart==n and numend==n:
                combs.append("".join(path))
                return
            for edge in [')','(']:
                if edge=='(':
                    gen(n, path+['('], numstart+1, numend)
                else:
                    gen(n, path+[')'], numstart, numend+1)

        gen(n, [], 0, 0)
        return combs


            


