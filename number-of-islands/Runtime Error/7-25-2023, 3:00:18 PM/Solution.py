// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = [[False for _ in range(COLS)] for _ in range(ROWS]]

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, visited):
                    islands+=1

        return islands




       

        def dfs(row, col, visited):
            if row >= ROWS or col >= COLS:
                return False      
            if visited[row][col]:
                return False
            if grid[row][col] == 0:
                return False

            visited[row][col] = True
            return dfs(row+1, col, visited) or dfs(row-1, col, visited) or dfs(row, col+1, visited) or dfs(row, col-1, visited)

            




