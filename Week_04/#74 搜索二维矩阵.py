#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1 and len(matrix[0]) == 0: return False
        n, m = len(matrix), len(matrix[0])
        left, right = 0, n*m-1
        while left <= right:
            mid = (right + left) //2 
            if matrix[mid//m][mid%m] > target:
                right = mid -1
            elif matrix[mid//m][mid%m] < target:
                left = mid +1
            else:
                return True
        return False

