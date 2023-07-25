// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = set()
        nums.sort()

        for i in range(len(nums)):
            comp = -nums[i]

            L = 0
            R = len(nums)-1

            while(L<R):
                if L!=i and R!=i:
                    s = nums[L]+nums[R]
                    if s==comp:
                        ans.add([i,L,R])
                    elif s>comp:
                        R-=1
                    else:
                        L+=1
        return ans