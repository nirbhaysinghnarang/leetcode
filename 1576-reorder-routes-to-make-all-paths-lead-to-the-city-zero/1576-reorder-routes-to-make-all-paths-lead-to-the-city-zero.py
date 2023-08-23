class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b in connections:
            g[a].append((b, True))
            g[b].append((a, False))
        visited = set()
        num_reversals = 0
        print(g)
        def dfs(root):
            if root in visited:
                return
    
            neighbours = g[root]
            visited.add(root)
            for n, flag in neighbours:
                if n not in visited:
                    if flag:
                        nonlocal num_reversals
                        num_reversals+=1
                dfs(n)
            
        dfs(0)
        return num_reversals
            