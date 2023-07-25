// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_capacity = sum(weights)
        min_capacity = max(weights)
        # The range [min_capacity, max_capacity] is the search space.
        l, r = min_capacity, max_capacity
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
        numDays = 1
        weightCarried = 0 
        for w in weights:
            weightCarried+=w
            if(weightCarried>capacity):
                weightCarried=w
                numDays+=1
            if(numDays>days):
                return False
        return True
        


