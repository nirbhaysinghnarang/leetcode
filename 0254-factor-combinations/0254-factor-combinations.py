class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def dfs(n, start, path, result):
            for i in range(start, int(n**0.5) + 1):
                if n % i == 0:
                    path.append(i)
                    path.append(n // i)
                    result.append(path[:])
                    path.pop()
                    dfs(n // i, i, path, result)
                    path.pop()

        result = []
        dfs(n, 2, [], result)
        return result
