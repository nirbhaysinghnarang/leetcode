class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        number = 0
        seq = set() 

        hm = Counter(tiles)

        def dfs(c):
            nonlocal number
            for k in c:
                if c[k] > 0:
                    c[k]-=1
                    dfs(c)
                    number+=1
                    c[k]+=1
        dfs(hm)
        return number
            

