// https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def isPal(s):
            print(s)
            return s==s[::-1]

        def dfs(index, partition):
            if index==len(s):
                ans.append(partition)
                return

            for i in range(index, len(s)):
                if isPal(s[index:i+1]):
                    partition.append(s[index:i])
                    dfs(i, partition)
                    partition.pop()

        dfs(0, [])
        return ans