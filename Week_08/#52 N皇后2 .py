#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def DFS(n, row, col, pie, na):
            if row >= n:
                self.count += 1
                return 
            bits = (~(col|pie|na)) &((1 << n)-1 ) #得到当前所有的码
            while bits:
                p = bits & -bits #取到最低位的1
                bits = bits & (bits -1) #表示在p位置放入皇后
                DFS(n, row+1, col|p,(pie|p)<< 1, (na|p)>>1)

        if n < 1: return []
        self.count = 0
        DFS(n, 0, 0, 0, 0)
        return self.count

