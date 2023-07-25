// https://leetcode.com/problems/find-if-path-exists-in-graph

from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = defaultdict(list)

        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        self.flag = 0

        @lru_cache(None)
        def solve(node):
            if node == destination:
                self.flag = 1
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    solve(i)
        solve(source)
        
        if self.flag:
            return True
        return False