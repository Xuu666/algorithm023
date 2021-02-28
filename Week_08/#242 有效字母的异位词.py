#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for j in t:
            if j not in dic: 
                return False
            else:
                dic[j] -= 1
        for i in dic.values():
            if i != 0: return False
        return True

