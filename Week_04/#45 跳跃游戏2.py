#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if len(nums) == 1: return 0
        maxlen,end,step = 0,0,0
        n = len(nums)
        for i in range(n-1):
            if i <= maxlen:
                maxlen = max(maxlen, i+nums[i])
                if i == end:
                    step += 1
                    end = maxlen
        return step

