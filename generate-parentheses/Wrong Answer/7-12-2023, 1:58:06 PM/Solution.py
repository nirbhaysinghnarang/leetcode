// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combs = []
        def gen(n, path, numstart, numend):
            if numstart==n or numend==n:
                combs.append("".join(path))
                return
            edges = ['(' for _ in range(n-numstart)]+[')' for _ in range(n-numend)]

            for edge in edges:
                if edge=='(':
                    gen(n, path+[edge], numstart+1, numend)
                else:
                    gen(n, path+[edge], numstart, numend+1)

        gen(n, [], 0, 0)
        return combs


            


