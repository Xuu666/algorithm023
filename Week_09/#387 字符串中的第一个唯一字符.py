#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch,0) + 1
        for i in range(len(s)):
            if dic[s[i]] == 1: 
                return i
                break
        return -1

