// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix

import functools
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def is_weaker(r1, r2):
            return dic[r1]<dic[r2] or (dic[r1]==dic[r2] and r1<r2)
            
        def count_soldiers(mat,r1):
            cnt = 0
            for elem in mat[r1]:
                if(elem!=0):
                    cnt+=1
                else:
                    return cnt
            
        soldiers_dic = {}
        for i in range(len(mat)-1):
            soldiers_dic[i] = count_soldiers(mat, i)
        rows = list(soldiers_dic.keys())
        rows = sorted(rows, key=functools.cmp_to_key(is_weaker))
        return rows[:k]


        


    
