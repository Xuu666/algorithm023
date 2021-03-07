#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.strip().split()[::-1])

