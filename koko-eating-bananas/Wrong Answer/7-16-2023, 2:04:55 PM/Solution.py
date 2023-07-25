// https://leetcode.com/problems/koko-eating-bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)

        ans_index = 0

        while(L<=R):
            mid = (L+R)//2
            #if koko can eat all bananas with this speed
            if(self.canEatAll(piles, h, mid)):
                ans_index = mid
                R = mid-1
            else:
                L = mid+1

        return ans_index

    def canEatAll(self, piles, hours, k):
        return sum(piles) <= hours*k
