from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        
        ROWS, COLS = len(rooms), len(rooms[0])
        INF = 2147483647
        gates = deque()

        # Find all gate locations (rooms with value 0) and add them to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    gates.append((r, c))

        # Perform BFS from all gate locations
        while gates:
            r, c = gates.popleft()
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and rooms[new_r][new_c] == INF:
                    rooms[new_r][new_c] = rooms[r][c] + 1
                    gates.append((new_r, new_c))
