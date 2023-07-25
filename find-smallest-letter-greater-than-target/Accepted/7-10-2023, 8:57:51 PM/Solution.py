// https://leetcode.com/problems/find-smallest-letter-greater-than-target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)-1
        boundary_index = 0
        while(l<=r):
            mid = (l+r)//2
            if(letters[mid]>target):
                r = mid - 1
                boundary_index = mid
            else:
                l = mid+1
            
        return letters[boundary_index]
