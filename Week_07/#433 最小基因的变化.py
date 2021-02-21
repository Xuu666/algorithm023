#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        if end not in bank: return -1
        q = [(start,0)]
        change = {'A':'CTG','C':'ATG','T':'ACG','G':'ACT'}
        while q:
            node, step = q.pop(0)
            if node == end: return step
            for i, v in enumerate(node):
                for j in change[v]:
                    new = node[:i] + j + node[i+1:]
                    if new in bank:
                        q.append((new,step+1))
                        bank.remove(new)
        return -1

