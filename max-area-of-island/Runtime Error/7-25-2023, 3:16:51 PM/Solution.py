// https://leetcode.com/problems/max-area-of-island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 

        ROWS = len(grid)
        COLS = len(grid[0])
        curr_area = 1

        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, curr_area):
            if not (0<=r<ROWS) or not (0<=c<COLS):
                return

            if visited[r][c]:
                return

            if grid[r][c]==0:
                return
            
            visited[r][c] = True
            nonlocal curr_area
            curr_area+=1  

            dfs(r+1, c, curr_area)
            dfs(r-1,c,curr_area)
            dfs(r,c+1, curr_area)
            dfs(r,c-1, curr_area)


        for r in range(ROWS):
            for c in range(COLS):
                if not visited[r][c] and grid[r][c]==1:
                    curr_area = 1
                    dfs(r,c,curr_area)
                    max_area = max(max_area, curr_area)


        return max_area
            

