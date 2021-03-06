#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums)-1
        while left < right:
            mid = (right+left)//2 
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[left]

