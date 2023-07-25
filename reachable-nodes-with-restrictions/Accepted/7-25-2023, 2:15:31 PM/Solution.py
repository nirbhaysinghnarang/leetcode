// https://leetcode.com/problems/reachable-nodes-with-restrictions

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        res_set = set()
        for node in restricted:
            res_set.add(node)

        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        count = 0

        visited = set()

        def dfs(node, visited):
            if node in visited:
                return
            nonlocal count 
            count+=1
            visited.add(node)
            for n in graph[node]:
                if n not in res_set:
                    dfs(n, visited)

        dfs(0, visited)
        return count
                    

                