#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = collections.defaultdict(list)
        for st in strs:
            s_key = [0] * 26
            for c in st:
                s_key[ord(c)-ord('a')] += 1
            dict[tuple(s_key)].append(st)
        return list(dict.values())

