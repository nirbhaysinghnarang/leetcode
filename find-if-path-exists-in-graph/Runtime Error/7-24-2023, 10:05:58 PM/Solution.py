// https://leetcode.com/problems/find-if-path-exists-in-graph

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def dfs(index):
            print(index)
            if index==destination:
                return True

            neighbours = edges[index]
            for neighbour in neighbours:
                dfs(neighbour)
        if dfs(source):
            return True
        return False