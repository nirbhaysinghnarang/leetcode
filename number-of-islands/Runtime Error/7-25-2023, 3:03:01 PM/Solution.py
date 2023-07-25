// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]


        def dfs(row, col, visited):
            if row >= ROWS or col >= COLS:
                return       
            if visited[row][col]:
                return 
            visited[row][col] = True
            dfs(row+1, col, visited) 
            dfs(row-1, col, visited) 
            dfs(row, col+1, visited) 
            dfs(row, col-1, visited)

            

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, visited):
        
        print(visited)

        return islands




       





