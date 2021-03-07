#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pn, sn = len(p) + 1, len(s) + 1
        dp = [[False] * pn for _ in range(sn)]
        print(pn,sn)
        print(dp)
        dp[0][0] = True
        for k in range(1,pn):
            if p[k-1] == "*":
                dp[0][k] = dp[0][k-1]
        for m in range(1,sn):
            for n in range(1,pn):
                if s[m-1] == p[n-1] or p[n-1] == "?":
                    dp[m][n] = dp[m-1][n-1]
                elif p[n-1] == "*":
                    dp[m][n] = dp[m-1][n] or dp[m][n-1]
        return dp[-1][-1]

