class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combs = []
        candidates.sort()
        def dfs(index, lst, curr_sum):
            if curr_sum==target:
                if not sorted(lst) in combs:
                    combs.append(lst)
                return
            for (i,edge) in enumerate(candidates):
                if curr_sum<target:
                    dfs(i, lst+[edge], curr_sum+candidates[i])

        dfs(0, [],0)
        return combs




            

                    

        