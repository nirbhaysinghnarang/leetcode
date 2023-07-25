// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
    
        def dfs(row, column, wordSoFar):
            if len(wordSoFar)>len(word):
                return False
            if wordSoFar==word:
                return True
            moves = [(0,1),(1,0), (0,-1),(-1,0)]
            for x,y in moves
                try:
                    if board[x][y] in word:
                        dfs(x,y, wordSoFar+board[row][column])
                except:
                    continue

            
        for x in range(m):
            for y in range(n):
                if word[0] == board[x][y]:
                    if dfs(x,y,""):
                        return True

        return False

