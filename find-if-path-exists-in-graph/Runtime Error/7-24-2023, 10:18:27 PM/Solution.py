// https://leetcode.com/problems/find-if-path-exists-in-graph

from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for i in arr:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        visited = set()
        
        def dfs(index):
            if index==destination:
                return True
            visited.add(index)
            for neighbour in graph[index]:
                if not neighbour in visited:
                    dfs(neighbour)
            
        
        if dfs(source):
            return True
        return False