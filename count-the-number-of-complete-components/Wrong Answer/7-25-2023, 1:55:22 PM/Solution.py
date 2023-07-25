// https://leetcode.com/problems/count-the-number-of-complete-components

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def findComponentsDFS(visited, components, graph):
            for node in range(n):
                if node not in visited:
                    connected_component = []
                    DFS(node, visited, connected_component, graph)
                    components.append(connected_component.copy())
    

        def DFS(node, visited, nodes_in_component, graph):
            if node in visited:
                return
            nodes_in_component.append(node)
            visited.add(node)
            neighbours = graph[node]
            for n in neighbours:
                DFS(n, visited, nodes_in_component, graph)

        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)


        components = []
        visited = set()
        findComponentsDFS(visited, components, graph)
        cnt = 0
        for component in components:
            num_nodes = len(component)
            edges = 0
            for node in component:
                print(graph[node])
                edges+=len(graph[node])

            if edges == (num_nodes * (num_nodes-1)) / 2:
                cnt+=1

        return cnt




       