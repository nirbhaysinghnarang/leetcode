class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        vis = set()
        def dfs(r,c):
            vis.add((r,c))
            for d_x, d_y in dirs:
                new_x, new_y = r+d_x, c+d_y
                if (new_x,new_y) not in vis and 0<=new_x<len(grid) and 0<=new_y<len(grid[0]) and grid[new_x][new_y]=='1':
                    dfs(new_x, new_y)

        islands=0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if not (x,y) in vis and grid[x][y]=='1':
                    dfs(x,y)
                    islands+=1
        print(grid)
        return islands
