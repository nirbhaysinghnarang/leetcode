// https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        lst = []

        def isPal(s):
            return s == s[::-1]

        def dfs(index, path):
            if index==len(s):
                lst.append("".join(path[:]))

            for edge in range(index+1, len(s)-1):
                if not isPal(s[index:edge]):
                    continue
                else:
                    path.append(s[index])
                    dfs(index+edge, path)
                    path.pop()
            
        dfs(0, [])
        return lst
