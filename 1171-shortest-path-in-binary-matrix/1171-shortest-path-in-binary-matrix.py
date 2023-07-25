from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs = [
            [0,1],
            [1,0],
            [0,-1],
            [-1,0],
            [1,-1],
            [-1,1],
            [1,1],
            [-1,-1]
        ]
        START_POS = (0,0)
        visited = set()
        q = deque()
        q.append(START_POS)
        visited.add(START_POS)
        ROWS = len(grid)
        COLS = len(grid[0])
        length = 1

        if grid[0][0]!=0:
            return -1

        while (len(q) > 0):
            for _ in range(len(q)):
                row, col = q.popleft()
                if row == ROWS-1 and col == COLS-1:
                    return length
                for delta_row, delta_col in dirs:
                    new_row, new_col = row+delta_row, col+delta_col
                    if new_row <0 or new_row >= ROWS or new_col < 0 or new_col >= COLS:
                        continue
                    if (new_row, new_col) in visited:
                        continue
                    if grid[new_row][new_col] == 1:
                        continue
                    q.append((new_row, new_col))
                    visited.add((new_row, new_col))
            length+=1
        return -1
        
