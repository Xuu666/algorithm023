#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 2
        for i in range(n-1):
            a, b = b, a+b 
        return a

