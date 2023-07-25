// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)-1
        n = len(board[0])-1
        def dfs(r, c, w):
            if w==word:
                print(w)
                return True
        
            hor_mov = [max(0,r-1), min(m, r+1)]
            ver_mov = [max(0, c-1), min(n, c+1)]
            for i in hor_mov:
                for j in ver_mov:
                    if i!=r and not board[i][c] in w:
                        if dfs(i,c, w+board[r][c]):
                            return True
                    if j!=c and not board[r][j] in w:
                        if dfs(r, j, w+board[r][c]):
                            return True
        if dfs(0,0,""):
            print("here")
            return True
        return False