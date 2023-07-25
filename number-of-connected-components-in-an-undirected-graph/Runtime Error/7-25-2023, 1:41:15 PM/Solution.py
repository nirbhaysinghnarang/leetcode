// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

class Solution:
   


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node, visited, edges):
            connections = edges[node]
            visited.add(node)
            for connection in connections:
                if connection not in visited:
                    dfs(connection, visited, edges)

        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(b)

        components = 0
        visited = set()

        for node in range(n):
            if node not in visited:
                dfs(node, visited, edges)
                components+=1

        return components


      