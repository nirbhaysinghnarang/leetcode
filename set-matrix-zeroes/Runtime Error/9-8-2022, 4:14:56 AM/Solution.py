// https://leetcode.com/problems/set-matrix-zeroes

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for col in range(len(row)):
                if matrix[row][col]==0:
                    self.makeRowZero(matrix, row)
                    self.makeColZero(matrix, col)
    
    
    def makeRowZero(self, matrix, rowIdx):
        for j in range(len(matrix)):
            matrix[rowIdx][j] = 0
            
    def makeColZero(self, matrix, colIdx):
        for j in range(len(matrix[0])):
            matrix[j][colIdx] = 0
        