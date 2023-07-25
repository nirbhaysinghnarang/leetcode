// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def dfs(r, c, w):
            if w==word:
                return True
            print(range(max(0, r-1), min(r+1, m)))
            for i in range(max(0, r-1), min(r+1, m)):
                for j in range(max(0, c-1), min(c+1,n)):
                    if(i!=r and j!=c):
                        dfs(i, j, w+board[i][j])


        dfs(0,0,"")
        return False