// https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        L, R = 0,0
        window_set = set()

        while(R<len(nums)):
            print(L, R, window_set)
            if R-L+1 > k:
                window_set.remove(nums[L])
                L+=1
            if nums[R] in window_set:
                return True
            window_set.add(nums[R])
            R+=1
        return False