// https://leetcode.com/problems/find-if-path-exists-in-graph

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def dfs(index):
            if index==destination:
                return True

            adjacent = edges[index]
            for edge in adjacent:
                dfs(edge[1])
        
        if dfs(source):
            return True
        return False