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
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for i in t:
            if i not in dict:
                return False
            else:
                dict[i] -= 1
        for i in dict.values():
            if i != 0:
                return False
        return True

