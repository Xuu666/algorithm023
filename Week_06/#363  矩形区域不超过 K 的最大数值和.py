#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import bisect
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(col):
            nums =[0] * row
            for right in range(left,col):
                for i in range(row):
                    nums[i] += matrix[i][right]
                array = [0]
                cum = 0
                for num in nums:
                    cum += num
                    loc = bisect.bisect_left(array, cum-k )
                    print(loc)
                    if loc < len(array):
                        res = max(res, cum - array[loc])
                    bisect.insort(array,cum)
        return res

