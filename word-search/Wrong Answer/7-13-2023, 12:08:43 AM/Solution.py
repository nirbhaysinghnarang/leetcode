// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)-1
        n = len(board[0])-1
        def dfs(r, c, w):
            print(w)
            if w==word:
                return True

            if len(w)>len(word):
                return False
        
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

        for i in range(m):
            for j in range(n):
                if dfs(i,j,""):
                    return True
        return False