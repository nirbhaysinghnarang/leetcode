// https://leetcode.com/problems/number-of-provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        provinces = 0
        visited = set()

        for city in range(n):
            if city not in visited:
                dfs(city, visited)
                provinces+=1
        
        return provinces

        def dfs(node, visited):
            if node in visited:
                return
            visited.add(node)
            for n in isConnected[node]:
                if n==1:
                    dfs(n, visited)

            
