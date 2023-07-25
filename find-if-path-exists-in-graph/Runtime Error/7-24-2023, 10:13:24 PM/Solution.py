// https://leetcode.com/problems/find-if-path-exists-in-graph

from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
       graph = defaultdic(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(b)
        
        print(graph)
        def dfs(index):
            if index==destination:
                return True
            for neighbour in graph[index]:
                dfs(neighbour)
        
        if dfs(source):
            return True
        return False