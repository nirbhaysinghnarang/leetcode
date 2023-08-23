class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        q = deque()
        visited = set()
        m = len(maze) - 1
        n = len(maze[0]) - 1

        q.append(tuple(entrance))
        visited.add(tuple(entrance))

        steps = 0
        while q:
            for _ in range(len(q)):
                c_x, c_y = q.popleft()
                if (c_x, c_y) != tuple(entrance) and (c_x == 0 or c_x == m or c_y == 0 or c_y == n):
                    return steps
                for del_x, del_y in dirs:
                    n_x, n_y = c_x + del_x, c_y + del_y
                    if 0 <= n_x <= m and 0 <= n_y <= n and maze[n_x][n_y] == "." and (n_x, n_y) not in visited:
                        q.append((n_x, n_y))
                        visited.add((n_x, n_y))
            steps += 1
        return -1