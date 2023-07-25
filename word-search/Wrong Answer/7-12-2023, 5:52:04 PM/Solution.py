// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r, c, w):
            print(w)
            if w==word:
                return True
            
            for i in range(len(board)):
                for j in range(len(board[0])):
                    dfs(i,j, w+board[i][j])

        return False