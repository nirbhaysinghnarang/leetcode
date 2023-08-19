class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_paths = 0
        memo = {} 
        
        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                return 1  
                
            if (x, y) in memo:
                return memo[(x, y)]
            
            dirs = [(0, 1), (1, 0)]
            total_paths = 0
            for del_x, del_y in dirs:
                new_x, new_y = x + del_x, y + del_y
                if new_x < m and new_y < n:
                    total_paths += dfs(new_x, new_y)
            
            memo[(x, y)] = total_paths
            return total_paths

        return dfs(0,0)
