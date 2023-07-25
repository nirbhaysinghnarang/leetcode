// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
    
        def dfs(row, column, wordSoFar):
            print(wordSoFar)
            if wordSoFar==word:
                return True
            hor_moves = [max(0, row-1), min(n-1, row+1)]
            ver_moves = [max(0, column-1), min(m-1, column+1)]

            for x in hor_moves:
                for y in ver_moves:
                    if board[x][y] in word:
                        dfs(x,y, wordSoFar+board[row][column])

            
        for x in range(m):
            for y in range(n):
                if word[0] == board[x][y]:
                    if dfs(x,y,""):
                        return True

        return False

