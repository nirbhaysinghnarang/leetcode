// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combs = []
        def dfs(st, so_far, o):
            if(len(so_far)==2*n):
                print(so_far)
                combs.append(so_far)
                return
            if o==0:
                dfs(st+1, so_far+'(',1)
            else:
                dfs(st+1, so_far+')', n-o-1)

        dfs(0,'',0)
        return combs

            


