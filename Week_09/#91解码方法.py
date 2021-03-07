#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp= [1,0]
        n = len(s)
        if n == 0: return 0
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(1,n):
            dp.append(0)
            if s[i] != '0':
                dp[i+1] += dp[i]
            if s[i-1:i+1] >= '10' and s[i-1:i+1]<= '26': 
                dp[i+1] += dp[i-1]
        return dp[-1]

