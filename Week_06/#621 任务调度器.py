#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = collections.Counter(tasks)
        maxExec = max(freq.values())
        maxcount = sum(1 for v in freq.values() if v == maxExec)
        return max((maxExec-1)*(n+1) + maxcount, len(tasks))

