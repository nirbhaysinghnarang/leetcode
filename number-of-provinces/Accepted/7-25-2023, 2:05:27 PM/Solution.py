// https://leetcode.com/problems/number-of-provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(node, visited):
            print("node:", node)
            if node in visited:
                return
            visited.add(node)
            for (i,n) in enumerate(isConnected[node]):
                if n==1:
                    dfs(i, visited)

        provinces = 0
        visited = set()

        n = len(isConnected)
        for city in range(n):
            if city not in visited:
                dfs(city, visited)
                provinces+=1
        
        return provinces

      
            
