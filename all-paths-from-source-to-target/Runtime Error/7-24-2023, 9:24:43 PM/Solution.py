// https://leetcode.com/problems/all-paths-from-source-to-target

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)-1
        paths = []
        def dfs(i, path):
            if i==n:
                paths.append(path)
                return

            neighbours = graph[i]
            for n in neighbours:
                path.append(n)
                dfs(n, path)
                path.pop()

        dfs(0, [])
        return paths