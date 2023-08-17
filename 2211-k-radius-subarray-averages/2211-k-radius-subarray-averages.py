class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k==0:
            return nums
        def getPrefixSum(nums):
            arr = [0]
            tot = 0
            for n in nums:
                tot+=n
                arr.append(tot)
            return arr
        win_size = (2*k)+1
        ps = getPrefixSum(nums)
        print(ps)
        ret = []
        for (i, num) in enumerate(nums):
            if i<k or i>=len(nums)-k:
                ret.append(-1)
            else:
                ret.append((ps[i+k+1] - ps[i-k])//(win_size))
        return ret


        