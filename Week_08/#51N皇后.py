#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 1: return
        result = []
        cols, pie, na = set(), set(),set()
        def DFS( n, row, cur_state):
            if row >= n:
                result.append(cur_state)
                return
            for col in range(n):
                if col in cols or row + col in pie or row - col in na: continue
                cols.add(col)
                pie.add(col + row)
                na.add(row - col)
                DFS(n, row + 1, cur_state + [col])
                cols.remove(col)
                pie.remove(row + col)
                na.remove(row - col)

        def generateresult(n):
            board = []
            for res in result:
                for i in res:
                    board.append('.'* i + 'Q' + '.'*(n -i - 1))
            #print(board)
            return [board[i:i+n] for i in range(0, len(board),n)]

        DFS(n, 0, [])
        return generateresult(n)

