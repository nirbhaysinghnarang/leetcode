// https://leetcode.com/problems/restore-ip-addresses

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        soln = []

        def dfs(i, path, num_ints):
            if num_ints==0 and i==len(s):
                soln.append(".".join(path.copy()))
                return 
            for x in range(i, min(i+3, len(s))):
                integer = int(s[i:x+1])
                int_str = s[i:x+1]
                if 0<=integer<=255 and not (len(int_str)>1 and int_str[0]=="0"):
                    path.append(str(integer))
                    dfs(x+1, path, num_ints-1)
                    path.pop()

        dfs(0, [], 4)
        return soln
            