class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #equiv to finding longest subarray with at most 2 distinct elems

        sz = 0
        L = 0
        win_set = Counter()
        for R in range(len(fruits)):
            win_set[fruits[R]]+=1
            while len(win_set) > 2:
                win_set[fruits[L]]-=1
                if win_set[fruits[L]]==0:
                    del win_set[fruits[L]]
                L+=1
            sz = max(R-L+1, sz)
        return sz