#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        size=len(s)
        if len(s)<2: return s
        dp=[[False for _ in range(size)] for _ in range(size)]
        max_len=1
        start=0
        for i in range(size):
            dp[i][i]=True

        for j in range(1,size):
            for i in range(0,j):
                if s[i]==s[j]:
                    if j-i<3:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j]=False

                if dp[i][j]:
                    cur_len=j-i+1
                    if cur_len>max_len:
                        max_len=cur_len
                        start=i
                        print(start)
        return s[start:start+max_len]

