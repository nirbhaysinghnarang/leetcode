// https://leetcode.com/problems/reshape-the-matrix

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        newMatrix = []
        flattened_list = []
        for row in matrix:
            for item in row:
                flattened_list.append(item)
        tracker = 0
        for i in range(r):
            newRow = []
            for j in range(c):
                newRow.append(flattened_list[tracker])
                tracker+=1
            newMatrix.append(newRow)
        return newMatrix