class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        return self.optimise(spells, potions, success)

    def naive(self, spells, potions, success):
        pairs = [-1 for _ in range(len(spells))]

        for (i,spell) in enumerate(spells):
            count = 0
            for potion in potions:
                if potion*spell>=success:
                    count+=1
            pairs[i] = count

        return pairs


    def optimise(self, spells, potions, success):
        potions = sorted(potions, reverse=True)
        pairs = [-1 for _ in range(len(spells))]
        for (i,spell) in enumerate(spells):
            L,R = 0, len(potions)-1
            count = 0
            while(L<=R):
                mid = (R+L)//2
                if spell*potions[mid] >= success:
                    count+=(mid-L+1)
                    L = mid+1
                else:
                    R = mid-1
            pairs[i] = count

        return pairs

        


            