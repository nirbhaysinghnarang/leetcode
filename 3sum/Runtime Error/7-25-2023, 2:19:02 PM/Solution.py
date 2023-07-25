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
                        break
                    elif s>comp:
                        R-=1
                    else:
                        L+=1
        return ans


     def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers)-1
        while(L<R):
            s = numbers[L]+numbers[R]
            if s == target:
                return [L+1, R+1]
            if s < target:
                L += 1
            else: 
                R -= 1

        return [L, R]
