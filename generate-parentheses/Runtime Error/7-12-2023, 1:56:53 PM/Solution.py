// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combs = []
        def gen(n, path, numstart, numend):
            if numstart==n or numend==n:
                combs.append("".join(path))
                return
            edges = ['(' for _ in range(numstart)]+[')' for _ in range(numend)]
            for edge in edges:
                if edge=='(':
                    dfs(n+1, path+[edge], numstart+1, numend)
                else:
                    dfs(n+1, path+[edge], numstart, numend+1)
                path.pop()

        gen(n, [], 1, 1)
        return combs


            


