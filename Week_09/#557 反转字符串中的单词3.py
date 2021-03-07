#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join (word[::-1] for word in s.split(" "))

