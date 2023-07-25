// https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        ans = -1
        while(l<=r):
            mid = (l+r)//2
            if(isBadVersion(mid)):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans