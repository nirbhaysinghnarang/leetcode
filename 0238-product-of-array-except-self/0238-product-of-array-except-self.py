class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        pref_prod = []
        suffix_prod = []

        prefix_product = 1
        suffix_product = 1


        for n in nums:
            pref_prod.append(prefix_product)
            prefix_product*=n

        for n in nums[::-1]:
            suffix_prod.append(suffix_product)
            suffix_product*=n

        suffix_prod = suffix_prod[::-1]
        for(a,b) in zip(pref_prod, suffix_prod):
            ret.append(a*b)
        return ret
        
      