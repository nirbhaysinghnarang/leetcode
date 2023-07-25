// https://leetcode.com/problems/restore-ip-addresses

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        soln = []

        def dfs(i, path):
            if i==len(s):
                soln.append(".".join(path.copy()))
                return

            for x in range(i, min(i+3, len(s))):
                path.append(s[i:x+1])
                dfs(x+1, path)
                path.pop()

        dfs(0, [])
        return soln
            