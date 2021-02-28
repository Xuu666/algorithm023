#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res, count = 0, 32
        while count:
            res <<= 1
            res += n & 1
            n >>= 1
            count -= 1
        return res

