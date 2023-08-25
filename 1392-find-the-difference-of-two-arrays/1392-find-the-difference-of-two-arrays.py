class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        c1 = set(Counter(nums1).keys())
        c2 = set(Counter(nums2).keys())

        return [
            [i for i in c1 if i not in c2],
            [i for i in c2 if i not in c1],
        ]