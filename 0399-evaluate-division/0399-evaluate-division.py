class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        variables = set()
        for i,(a,b) in enumerate(equations):
            g[a].append((b, values[i]))
            g[b].append((a, (1/values[i]))) 
            variables.add(a)
            variables.add(b)
        def getValue(quot, div,visited, prod_so_far=1):
            if quot not in variables or div not in variables:
                return -1
            if quot == div:
                return prod_so_far
            neighbours = g[quot]
            visited.add(quot)
            for n, runner in neighbours:
                if n not in visited:
                    tmp = getValue(n, div, visited,prod_so_far*runner)
                    if tmp!=-1:
                        return tmp
            return -1
        arr = []
        for q,div in queries:
            visited = set()
            arr.append(getValue(q,div, visited))
        return arr

            
            
