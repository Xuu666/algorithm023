#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.cnt = 0
        self.mergesort(nums,0,len(nums) - 1)
        return self.cnt

    def mergesort(self, nums, L, R):
        if L < R:
            mid = L + (R - L) //2
            self.mergesort(nums, L, mid)
            self.mergesort(nums, mid+1, R)
            self.merge(nums, L, mid, R)
            #print(L,R, mid, self.cnt)

    def merge(self, nums, L, mid, R):
        i, j = L, mid+1
        tmp = []
        while i <= mid and j <= R:
            if nums[i] <= nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        #计数翻转对---------------
        ii, jj = L, mid+1
        while ii <= mid and jj <= R:
            if nums[ii] <= 2*nums[jj]:
                ii += 1
            else:
                self.cnt += (mid - ii +1)
                jj += 1
        #---------------------
        if i <= mid: tmp += nums[i:mid+1]
        if j <= R: tmp += nums[j:R+1]
        for i in range(len(tmp)):
            nums[L+i] = tmp[i]

