class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """
        """
        L = 0
        max_R = -1
        max_L = -1
        s = 0
        for i,c in enumerate(customers):
            if grumpy[i]==0:
                s+=c
                customers[i] = 0
        max_sat = s
        num_sat_in_window = s
        for R in range(len(customers)):
            win_sz = R-L+1
            num_sat_in_window += customers[R]
            while L<R and win_sz > minutes:
                num_sat_in_window -= customers[L]
                L+=1
                win_sz = R-L+1
            if num_sat_in_window > max_sat:
                max_sat = num_sat_in_window

        return max_sat
        
            


            


