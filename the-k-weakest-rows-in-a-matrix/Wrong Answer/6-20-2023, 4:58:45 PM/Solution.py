// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix

import functools
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
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
        def is_weaker(r1, r2):
            return soldiers_dic[r1]<soldiers_dic[r2] or (soldiers_dic[r1]==soldiers_dic[r2] and r1<r2)
            
        
            
        
        rows = list(soldiers_dic.keys())
        print(rows)
        rows = sorted(rows, key=functools.cmp_to_key(is_weaker))
        print(rows)
        return rows[:k]


        


    
