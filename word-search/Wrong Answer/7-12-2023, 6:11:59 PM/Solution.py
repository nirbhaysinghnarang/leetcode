// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)-1
        n = len(board[0])-1
        def dfs(r, c, w):
            print(w)
            if w==word:
                return True
        
            hor_mov = [max(0,r-1), min(m, r+1)]
            ver_mov = [max(0, c-1), min(n, c+1)]
            for i in hor_mov:
                for j in ver_mov:
                    if i!=r and j!=c and not board[i][j] in w:
                        dfs(i,j, w+board[r][c])


        dfs(0,0,"")
        return False