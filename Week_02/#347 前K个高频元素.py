#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        Hash={}
        for i in nums:
            Hash[i]=Hash.get(i,0)+1
        keyvalues=sorted(Hash.items(),key=lambda x:(x[1],x[0]),reverse=True)
        return [keyvalues[j][0] for j in range(k)]

