// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r, c, w):
            print(r,c,w)
            if w==word:
                return True
            
            for i in range(r,len(board)):
                    dfs(i, c, w+board[i][c])

            for j in range(c,len(board[0])):
                dfs(r, j, w+board[r][j])

                    

        return False