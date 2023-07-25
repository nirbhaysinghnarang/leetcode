// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def dfs(r, c, w):
            if w==word:
                return True
        

            for i in range(max(0, r-1), min(m, r+1)):
                for j in range(max(0, c-1), min(n, c+1)):
                    if i!=r and j!=c and not board[i][j] in w:
                        dfs(i,j, w+board[r][c])


        dfs(0,0,"")
        return False