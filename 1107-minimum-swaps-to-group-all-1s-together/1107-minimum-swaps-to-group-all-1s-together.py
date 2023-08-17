class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = 0
        for num in data:
            if num == 1: 
                ones+=1
        if ones==1:
            return 0
        min_count = float('inf')
        zeroes_in_window = 0
        L = 0
        for R in range(len(data)):
            if data[R]==0:
                zeroes_in_window+=1
            while R-L+1 > ones:
                if data[L] == 0:
                    zeroes_in_window = max(zeroes_in_window-1,0)
                L+=1
            if R-L+1 == ones:
                min_count = min(min_count, zeroes_in_window)

        return 0 if min_count == float('inf') else min_count

        