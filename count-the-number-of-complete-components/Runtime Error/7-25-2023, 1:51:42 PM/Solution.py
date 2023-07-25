// https://leetcode.com/problems/count-the-number-of-complete-components

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def findComponentsDFS(visited, components):
            for node in range(n):
                if node not in visited:
                    connected_component = []
                    DFS(node, visited, connected_component)
                    print(connected_component)
                    components.append(connected_component.copy())
    

        def DFS(node, visited, nodes_in_component):
            nodes_in_component.append(node)
            visited.add(node)
            neighbours = node[graph]
            for n in neighbours:
                DFS(n, visited, nodes_in_components)

        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)


        components = []
        visited = set()
        findComponentsDFS(visited, components)


       