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

        graph = Node()
        def dfs(node, cloned):
            cloned.val = node.val
            if not node.neighbours:
                cloned.neighbours = []
            else:
                for n in node.neighbours:
                    dfs(n, cloned)

        dfs(node, graph)
        return graph