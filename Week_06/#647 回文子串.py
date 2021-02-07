#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lens, res = len(s),0
        dp = [[0]*lens for _ in range(lens) ]
        for j in range(lens):
            for i in range(0,j+1):
                if i == j:
                    dp[i][j] = 1
                    res += 1
                elif j-i == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    res += 1
                elif s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                    res += 1
        return res

