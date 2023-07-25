// https://leetcode.com/problems/number-of-provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(node, visited):
            if node in visited:
                return
            visited.add(node)
            for n in isConnected[node]:
                if n==1:
                    dfs(n, visited)

        provinces = 0
        visited = set()

        n = len(isConnected)
        for city in range(n):
            print(isConnected[city])
            print(city in visited)
            if city not in visited:
                dfs(city, visited)
                provinces+=1
        
        return provinces

      
            
