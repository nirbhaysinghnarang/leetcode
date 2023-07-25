// https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        lst = []

        def isPal(s):
            return s == s[::-1]

        def dfs(index, path):
            if index==len(s):
                lst.append("".join(path[:]))
            for edge in range(index+1, len(s)+1):
                prefix = s[index:edge]
                if not isPal(prefix):
                    continue
                else:
                    dfs(edge, path+[prefix])
            
        dfs(0, [])
        return lst
