// https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def isPal(s):
            return s==s[::-1]

        def dfs(index, partition):
            if index==len(s):
                print(partition)
                ans.append(partition)
                return

            for i in range(index, len(s)):
                if isPal(s[index:i+1]):
                    partition.append(s[index:i+1])
                    dfs(i+1, partition)
                    partition.pop()

        dfs(0, [])
        return ans