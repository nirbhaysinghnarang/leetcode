class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRS = [(0,1),(1,0),(0,-1),(-1,0)]

    
        def dfs(r, c,index):
            if index == len(word):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[index]:
                return False

            original_char = board[r][c]
            board[r][c] = '#' 

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                if dfs(r + dr, c + dc, index + 1):
                    return True

            board[r][c] = original_char  

            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and dfs(r, c,0):
                    return True
        return False

