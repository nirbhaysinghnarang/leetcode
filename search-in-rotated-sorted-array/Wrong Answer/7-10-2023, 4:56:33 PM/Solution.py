// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.naive(nums, target)
        

    def naive(self, nums: List[int], target: int) -> int:
        """
        Algo: find sublists by finding pivot
        Run BS to sublists
        """

        l, r = 0, len(nums)
        pivot = -1

        while(l<=r):
            mid = (l+r)//2
            if(nums[mid] <= nums[-1]):
                pivot = mid
                r = mid-1
            else:
                l = mid+1

        print(pivot)
        left_ans = self.binary_search(nums[:pivot-1], target)
        right_ans = self.binary_search(nums[pivot:], target)

        if (left_ans == -1 and right_ans!=-1):
            return right_ans
        elif (left_ans!=-1 and right_ans==-1):
            return left_answer
        return -1


    
    def binary_search(self, nums, target):
        l, r = 0, len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid]==target):
                return mid
            elif (nums[mid]>target):
                r = mid-1
            else:
                l = mid+1
        return -1
            


