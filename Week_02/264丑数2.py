#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap=[]
        heapq.heappush(heap,1)
        seen=set()
        seen.add(1)
        factors=[2,3,5]
        curr_ugly=1
        for _ in range(n):
            curr_ugly=heapq.heappop(heap)
            for f in factors:
                new_ugly = f*curr_ugly
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap,new_ugly)
        return curr_ugly

