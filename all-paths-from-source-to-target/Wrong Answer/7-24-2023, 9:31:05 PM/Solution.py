// https://leetcode.com/problems/all-paths-from-source-to-target

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dest = len(graph)-1
        paths = []
        def dfs(i, path):
            if i==dest:
                paths.append(path.copy())
                return

            neighbours = graph[i]
            for n in neighbours:
                path.append(i)
                path.append(n)
                dfs(n, path)
                path.pop()
                path.pop()

        dfs(0, [])
        return paths