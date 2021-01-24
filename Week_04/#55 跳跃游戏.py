#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxlen = 0
        n = len(nums)
        for i in range(n):
            if i <= maxlen and i+nums[i] >= maxlen:
                maxlen = max(maxlen, i+nums[i])
                if maxlen >= n-1: return True
        return False

