#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five,ten = 0,0
        for i in bills:
            if i == 5: five += 1
            elif i == 10: five,ten = five-1, ten+1
            elif ten > 0:  five, ten = five-1,ten-1
            else: five -= 3
            if five <0: return False
        return True

