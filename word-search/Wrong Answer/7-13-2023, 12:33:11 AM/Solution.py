// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)-1
        n = len(board[0])-1
        def dfs(r, c, w, wordIndices):
            print(wordIndices)
            if board[r][c] not in word:
                return False
            if w+board[r][c]==word:
                return True
            if w==word:
                return True
            if len(w)>len(word):
                return False
        
            moves = [(1,0),(0,1),(0,-1),(-1,0)]
            for i,j in moves:
                if [i,j] not in wordIndices:
                    wordIndices.append([i,j])
                    if dfs(i,j,w+board[r][c], wordIndices):
                        return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,"",[]) and board[i][j]==word[0]:
                    return True
        return False