#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        val = [1] + nums + [1]
        rec = [[0] * (n+2) for _ in range(n+2)]
        for i in range (n-1,-1,-1):
            for j in range(i+2,n+2):
                for k in range(i+1,j):
                    total = val[i]*val[k]*val[j] + rec[i][k]+ rec[k][j]
                    rec[i][j] = max(rec[i][j],total)
        return rec[0][n+1]

