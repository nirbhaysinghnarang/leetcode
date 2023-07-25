// https://leetcode.com/problems/number-of-provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(node, visited):
            if node in visited:
                return
            visited.add(node)
            for n in isConnected[node-1]:
                if n==1:
                    dfs(n, visited)

        provinces = 0
        visited = set()


        n = len(isConnected)
        for city in range(1,n+1):
            if city not in visited:
                dfs(city, visited)
                provinces+=1
        
        return provinces

      
            
