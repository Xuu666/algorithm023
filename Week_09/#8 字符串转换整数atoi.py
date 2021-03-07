#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        MAX, MIN = 2 ** 31 -1, -2 ** 31
        import re 
        matches = re.match('[ ]*([+-]?\d+)', s)
        if matches:
            res = int(matches.group(1))
            if res > MAX: 
                return MAX
            elif res < MIN:
                return MIN
            else:
                return res
        return 0

