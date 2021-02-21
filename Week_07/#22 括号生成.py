#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backtrack(path = '',left = n,right = n):
            if right < left: return
            if left < 0 or right < 0: return
            if left == right == 0:
                res.append(path)
                return
            backtrack(path + '(',left - 1, right)
            backtrack(path + ')',left, right - 1)
        
        backtrack()
        return res

