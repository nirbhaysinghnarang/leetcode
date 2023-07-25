// https://leetcode.com/problems/find-if-path-exists-in-graph

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(a)
            graph[b].append(b)
            
        def dfs(index):
            if index==destination:
                return True
            for neighbour in graph[index]:
                dfs(neighbour)
        
        if dfs(source):
            return True
        return False