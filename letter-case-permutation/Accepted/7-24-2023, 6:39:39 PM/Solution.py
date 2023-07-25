// https://leetcode.com/problems/letter-case-permutation

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        perms = []

        def dfs(i, perm):
            if i==len(s):
                perms.append(''.join(perm.copy()))
                return

            char = s[i]
            if char.isalpha():
                options = [char.lower(), char.upper()]
            else:
                options = [char]

            for option in options:
                perm.append(option)
                dfs(i+1, perm)
                perm.pop()

        dfs(0, [])
        return perms

            