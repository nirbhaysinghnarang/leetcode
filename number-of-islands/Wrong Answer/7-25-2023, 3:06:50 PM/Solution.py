// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]


        def dfs(row, col):
            if row >= ROWS or row <0 or col >= COLS or col<0:
                return       
            if visited[row][col]:
                return 
            
            visited[row][col] = True

            if grid[row][col]==0:
                return

                
            dfs(row+1, col) 
            dfs(row-1, col) 
            dfs(row, col+1) 
            dfs(row, col-1)

            

        for r in range(ROWS):
            for c in range(COLS):
                if (not visited[r][c]) and grid[r][c]==1:
                    dfs(r, c)
                    islands+=1

        return islands




       





