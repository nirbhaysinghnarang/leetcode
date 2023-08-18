class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        result = 0
        graph = defaultdict(set)

        for road in roads:

            source , destination = road

            graph[source].add(destination)
            graph[destination].add(source)

        for node1 in range(n):
            for node2 in range(node1 + 1 , n):

                current_max = len(graph[node1]) + len(graph[node2])

                if node1 in graph[node2]:
                    current_max = current_max - 1

                result = max(result , current_max)

        return result
