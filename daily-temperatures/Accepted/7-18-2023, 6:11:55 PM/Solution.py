// https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for (i, t) in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                ans[stack[-1][0]] = i - stack[-1][0] 
                stack.pop()
            stack.append((i,t))
        return ans


    def naive(self, temperatures):
        ans = [0] * len(temperatures)
        hm = {}
        for (i,t) in enumerate(temperatures):
            hm[i] = t
        for (i,t) in enumerate(temperatures):
            min_idx = float('inf')
            for key in hm:
                if key > i and hm[key] > t:
                    min_idx = min(min_idx, key)
            ans[i] = 0 if min_idx == float('inf') else min_idx - i

        return ans




        
