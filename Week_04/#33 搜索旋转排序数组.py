#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: return -1
        left,right = 0, len(nums)-1
        while left < right:
            mid = (right-left)// 2 +left
            if nums[mid] == target: return mid
            if nums[mid] > nums[left]:
                if nums[left] <= target <= nums[mid]: 
                    right = mid
                else:
                    left = mid+1
            else:
                if nums[mid+1] <= target <= nums[right]:
                    left = mid +1
                else:
                    right = mid
        if nums[left] == target:
            return left 
        else:
            return -1

