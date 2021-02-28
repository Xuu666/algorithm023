#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key= lambda x:x[0])
        merged=[]
        for interval in intervals:
            if not merged or interval[0]>merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1]=max(merged[-1][1],interval[1])
        return merged

