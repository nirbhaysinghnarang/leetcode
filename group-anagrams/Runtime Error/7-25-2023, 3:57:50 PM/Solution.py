// https://leetcode.com/problems/group-anagrams

from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def isAnagram(p,q):
            return Counter(p) == Counter(q)
        res = []
        used = set()
        for s1 in strs:
            s = sorted(s1)
            if s not in used:
                ans = []
                for s2 in strs:
                    if isAnagram(s1, s2):
                        ans.append(s2)
                used.add(s)

        return res

            