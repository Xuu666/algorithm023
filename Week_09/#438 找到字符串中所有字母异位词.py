#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        window, needs = {}, {}
        for pi in p: needs[pi] = needs.get(pi,0) +1
        
        length, limit = len(p), len(s)
        left = right = 0

        while right < limit:
            c = s[right]
            if c not in needs:
                window.clear()
                left = right = right +1
            else:
                window[c] = window.get(c,0) +1
                if right - left + 1 == length:
                    if window == needs: res.append(left)
                    window[s[left]] -= 1
                    left += 1
                right += 1
        return res

