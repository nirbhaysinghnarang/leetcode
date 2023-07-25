// https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        curSum = 0
        cnt = 0
        for R in range(len(arr)):
            if R-L > k:
                curSum -= arr[L]
                L+=1

            avgOfWindow = curSum / (R-L)
            print(arr[L:R], avgOfWindow)
            if avgOfWindow >= threshold:
                cnt +=1


        return cnt

