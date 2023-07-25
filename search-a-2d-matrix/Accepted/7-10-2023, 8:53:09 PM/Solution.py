// https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Binary search
        Algo pseudocode:
        access middle row [mid]

        if last element of middle row is less than target
        then left = mid + 1 
        
        else right = mid -1
        """

        m = len(matrix)-1
        n = len(matrix[0])-1

        l, r = 0, m

        while(l<=r):
            mid = (l+r)//2
            row = matrix[mid]
            if self.searchRow(row, target):
                return True
            if row[n]<target:
                l = mid+1
            else:
                r = mid-1


    def searchRow(self, row: List[int], target: int) -> bool:
        l, r = 0, len(row)-1
        while(l<=r):
            mid = (l+r)//2
            if(row[mid]==target):
                return True
            elif row[mid]>target:
                r = mid -1
            else:
                l = mid +1

        return False