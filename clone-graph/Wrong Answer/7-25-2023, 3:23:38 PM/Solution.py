// https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = set()
        graph = Node()
        def dfs(node, cloned):
            if node in visited:
                return

            visited.add(node)
            cloned.val = node.val
            if not node.neighbors:
                cloned.neighbors = []
            else:
                for n in node.neighbors:
                    dfs(n, cloned)

        dfs(node, graph)
        node = graph
        print(graph)
        return node