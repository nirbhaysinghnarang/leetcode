// https://leetcode.com/problems/all-paths-from-source-to-target

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)-1
        print(n)
        paths = []
        def dfs(i, path):
            nonlocal n
            if i==n:
                print(path.copy())
                paths.append(path.copy())
                return

            neighbours = graph[i]
            for n in neighbours:
                path.append(n)
                dfs(n, path)
                path.pop()

        dfs(0, [])
        return paths