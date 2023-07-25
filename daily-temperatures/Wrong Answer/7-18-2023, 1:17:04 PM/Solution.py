// https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        hm = {}

        for (i,t) in enumerate(temperatures):

            hm[i] = t

        for (i,t) in enumerate(temperatures):
            min_idx = float('inf')
            for key in hm:
                if key > i and hm[key] > t:
                    ans[i] = min(min_idx, t)
            ans[i] = 0 if ans[i] == float('inf') else ans[i]

        return ans




        
