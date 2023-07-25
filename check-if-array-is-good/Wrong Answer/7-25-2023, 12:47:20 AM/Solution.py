// https://leetcode.com/problems/check-if-array-is-good

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = Counter()
        n = max(nums)
        for i in range(n):
            m[i]+=1

        m[n]+=1
        print(m)

        for num in nums:
            if m[num]==1:
                del m[num]
            else:
                m[num]-=1
        print(m)
        return m == {}
            