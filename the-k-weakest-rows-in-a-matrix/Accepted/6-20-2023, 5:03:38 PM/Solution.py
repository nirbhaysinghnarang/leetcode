// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix

import functools
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def count_soldiers(mat, r1):
            cnt = 0
            for elem in mat[r1]:
                if elem != 0:
                    cnt += 1
                else:
                    return cnt
            return cnt  # Added a return statement if all soldiers are present
        
        soldiers_dic = {}
        for i in range(len(mat)):  # Fixed the range to include the last row
            soldiers_dic[i] = count_soldiers(mat, i)

        def is_weaker(r1, r2):
            if soldiers_dic[r1] < soldiers_dic[r2]:
                return -1
            elif soldiers_dic[r1] > soldiers_dic[r2]:
                return 1
            elif r1 < r2:
                return -1
            elif r1 > r2:
                return 1
            else:
                return 0
        
        rows = list(soldiers_dic.keys())
        rows = sorted(rows, key=functools.cmp_to_key(is_weaker))
        return rows[:k]
