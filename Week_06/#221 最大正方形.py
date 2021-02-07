#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row,col =len(matrix),len(matrix[0])
        maxlen = 0
        dp = [[0]*(col+1) for _ in range(row+1)]
        for i in range(1,row+1):
            for j in range(1,col+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                else:
                    dp[i][j] = 0
                maxlen = max(dp[i][j],maxlen)
        return maxlen ** 2

