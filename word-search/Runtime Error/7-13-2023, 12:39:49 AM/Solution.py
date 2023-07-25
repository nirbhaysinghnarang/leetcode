// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)-1
        n = len(board[0])-1
        def dfs(r, c, wordAcc):
            if wordAcc==(word):
                return True
            if r<0 or r>m or c<0 or c>n:
                return False
            moves = [(0,1), (1,0), (-1,0), (0,-1)]
            for x,y in moves:
                if(dfs(r+x, c+y, wordAcc+[r][c])):
                    return True
                

            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,"") and board[i][j]==word[0]:
                    return True
        return False