class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_d = [0 for _ in range(n+1)]
        in_d = [0 for _ in range(n+1)]
        for a,b in trust:
            out_d[a]+=1
            in_d[b]+=1

        for x in range(1,n+1):
            if out_d[x] == 0 and in_d[x] == n-1:
                return x
        return -1


