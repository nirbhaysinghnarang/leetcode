// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)-1
        n = len(board[0])-1
        def dfs(r, c, wordAcc):
            print(wordAcc)
            if len(wordAcc)>len(word):
                return False
            if wordAcc==(word):
                return True
            if r<0 or r>m or c<0 or c>n:
                return False
            moves = [(0,1), (1,0), (-1,0), (0,-1)]
            for x,y in moves:
                try:
                    tmp = board[r+x][c+y]
                    if board[r+x][c+y]!=-1:
                        if(dfs(r+x, c+y, wordAcc+board[r][c])):
                            return True
                        else:
                            board[r+x][c+y]=temp
                except:
                    continue
                

                

            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,"") and board[i][j]==word[0]:
                    return True
        return False