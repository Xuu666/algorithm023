#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        leng = max(arr1) + 1 
        cnt = [0] * leng
        res = []
        for num in arr1:
            cnt[num] += 1
        for num in arr2:
            if cnt[num]: 
                res += [num] * cnt[num]
                cnt[num] = 0
        for num in range(leng):
            if cnt[num]: res += [num] * cnt[num]
        return res

