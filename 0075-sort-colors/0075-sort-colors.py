class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        c = Counter(nums)

        c = {
            0:c[0],
            1:c[1],
            2:c[2]
        }
        index = 0
        for i in range(c[0]):
            nums[index] = 0
            index+=1
        for i in range(c[1]):
            nums[index] = 1
            index+=1
        for i in range(c[2]):
            nums[index] = 2
            index+=1


        return nums

        