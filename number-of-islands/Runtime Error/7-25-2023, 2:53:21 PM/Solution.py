// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0

        visited = [[False for _ in range(len(grid[0])) for _ in range(len(grid))]]

        print(visited)