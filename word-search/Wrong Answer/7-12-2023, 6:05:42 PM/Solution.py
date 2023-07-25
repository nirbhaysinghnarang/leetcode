// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)-1
        n = len(board[0])-1
        def dfs(r, c, w):
            print(w)
            if w==word:
                return True


            horiz_mov = [max(0, r-1), min(m, r+1)]
            vert_mov = [max(0, c-1), min(n, c+1)]
            for i in horiz_mov:
                for j in vert_mov:
                    if i!=r and j!=c and len(w)<len(word):
                        dfs(i,j, w+board[r][c])


        dfs(0,0,"")
        return False