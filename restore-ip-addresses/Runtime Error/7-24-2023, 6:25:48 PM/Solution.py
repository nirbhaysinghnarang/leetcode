// https://leetcode.com/problems/restore-ip-addresses

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        soln = []

        def dfs(i, path):
            if i==len(s):
                soln.append(".".join(path.copy()))
                return

            for x in range(i, i+3):
                path.append(s[i:x])
                dfs(x+1, path)
                path.pop()

        dfs(0, [])
        return soln
            