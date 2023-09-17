class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        power_set = []


        def dfs(index, path):
            if index >= len(nums):
                power_set.append(path.copy())
                return

            path.append(nums[index])
            dfs(index+1, path)
            path.pop()


            dfs(index+1, path)

        dfs(0, [])
        return power_set

            