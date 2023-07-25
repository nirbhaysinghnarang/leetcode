// https://leetcode.com/problems/find-if-path-exists-in-graph

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def dfs(index):
            if index==destination:
                return True

            adjacent_edges = list(filter(edges, lambda x,y: x==index or y==index))
            print(adjacent_edges)
        if dfs(source):
            return True
        return False