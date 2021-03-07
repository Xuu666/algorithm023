#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res, flag = "", True
        for i in range(0, len(s), k):
            res += s[i:i+k][:: -1] if flag else s[i:i+k]
            flag = not flag
        return res

