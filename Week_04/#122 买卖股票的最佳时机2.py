#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1,len(prices)):
            tmp = prices[i]-prices[i-1]
            profit += max(tmp,0)
        return profit

