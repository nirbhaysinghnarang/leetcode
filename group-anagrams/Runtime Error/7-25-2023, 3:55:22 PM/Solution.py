// https://leetcode.com/problems/group-anagrams

from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def isAnagram(p,q):
            return Counter(p) == Counter(q)
        res = []
        for s1 in strs:
            ans = []
            for s2 in strs:
                if isAnagram(s1, s2)
                ans.append(s2)
            res.append(ans)

        return res

            