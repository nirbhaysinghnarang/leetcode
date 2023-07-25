// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def dfs(r, c, w):
            if w==word:
                return True
            
            for i in range(min(0, r-1), min(r+1, m)):
                for j in range(min(0, c-1), min(c+1,n)):
                    dfs(i, j, w+board[i][j])



        return False