// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combs = []

        def dfs(st, so_far, open_p, closed_p):
            if(len(so_far)==2*n):
                combs.append(so_far)
                return

            chars = ['(',')']
            if open_p<n:
                dfs(st+1, so_far+'(', open_p+1, closed_p)
            if closed_p<n:
                dsf(st+1, so_far+')', open_p, closed_p+1)
        dfs(0,"",0,0)
        return combs
                

            

            
        dfs(0, "", 0, 0)
        

            


