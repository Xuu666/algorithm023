#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums,size,depth,path,used,res):
            if depth == size: 
                res.append(path[:])
                return 
            for i in range(size):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue
                    used[i] = True
                    path.append(nums[i])
                    
                    dfs(nums,size,depth+1,path,used,res)

                    used[i] = False
                    path.pop()
        size = len(nums)
        if size == 0: return []
        nums.sort()
        used = [False for _ in range(size)]
        res = []
        dfs(nums,size,0,[],used,res)
        return res

