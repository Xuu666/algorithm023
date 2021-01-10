#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map={}
        for i in range(len(nums)):
            if (target-nums[i]) not in map:
                map[nums[i]]=i
            else:
                return map[target-nums[i]],i

