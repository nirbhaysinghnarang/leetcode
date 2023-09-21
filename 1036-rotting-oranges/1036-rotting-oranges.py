from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = -1
        visited = set()
        rotten = deque()
        num_fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [
            [0,1],
            [1,0],
            [0,-1],
            [-1,0]
        ]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c]==1:
                    num_fresh+=1

        if num_fresh == 0:
            return 0

        while rotten:
            minutes+=1
            for _ in range(len(rotten)):
                curr_r, curr_c = rotten.popleft()
                for del_r, del_c in dirs:
                    new_r, new_c = curr_r+del_r, curr_c+del_c
                    if 0>new_r or new_r >= ROWS or new_c <0 or new_c >= COLS:
                        continue
                    if (new_r, new_c) in visited:
                        continue
                    if grid[new_r][new_c] != 1:
                        continue
                    num_fresh-=1
                    grid[new_r][new_c] = 2
                    rotten.append((new_r, new_c))
                    visited.add((new_r, new_c))

        
        if num_fresh != 0:
            return -1

        return minutes
                    


        

        
                                                            





