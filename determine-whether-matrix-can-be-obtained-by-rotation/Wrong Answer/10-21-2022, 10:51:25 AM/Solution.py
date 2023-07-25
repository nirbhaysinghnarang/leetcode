// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation

class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        
        
        return set(tuple(i) for i in mat)==set(tuple(i) for i in target)