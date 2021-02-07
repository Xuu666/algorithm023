#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * max((n+1),3)
        mod = 10**9 + 7
        res = 0
        dp[0], dp[1],dp[2] = 1,2,4
        for i in range(3,n+1):
            dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]) % mod
        for i in range(1, n+1):
            res += (dp[i-1]*dp[n-i]) % mod 
        #if n % 2 == 1: res += dp[n/2]*dp[n/2]
        return (res + dp[n]) % mod

