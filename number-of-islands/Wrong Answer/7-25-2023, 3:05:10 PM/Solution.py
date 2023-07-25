// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]


        def dfs(row, col):
            if row >= ROWS or col >= COLS:
                return       
            if visited[row][col]:
                return 
            visited[row][col] = True
            dfs(row+1, col) 
            dfs(row-1, col) 
            dfs(row, col+1) 
            dfs(row, col-1)

            

        for r in range(ROWS):
            for c in range(COLS):
                if not visited[r][c]:
                    dfs(r, c)
                    islands+=1

        return islands




       





