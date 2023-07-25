// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_capacity = sum(weights)
        min_capacity = min(weights)
        # The range [min_capacity, max_capacity] is the search space.

        l, r = min_capacity, max_capacity
        print(l,r)
        answer_idx = -1
        while(l<=r):
            mid = (l+r)//2
            if self.canShip(mid, weights, days):
                answer_idx = mid
                r = mid-1
            else:
                l = mid+1
        return answer_idx


        
    def canShip(self, capacity, weights, days):
        totalSum=0
        for i in range(days):
            daySum = 0
            while(daySum<=capacity):
                for w in weights:
                    daySum+=w
            totalSum+=daySum
        if totalSum>=sum(weights):
            return True
        return False
        


