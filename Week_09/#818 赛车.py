#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        dp = [0,1] + [float('inf')] * target
        for t in range(2,target+1):
            k = t.bit_length()
            if t == 2 ** k -1:  dp[t] = k
            for j in range(k-1):
                dp[t] = min(dp[t],dp[ t- 2**(k-1) + 2**j] + k+j+1)
            dp[t] = min(dp[t] , dp[2**k -1-t]+k+1)
        return dp[target]

