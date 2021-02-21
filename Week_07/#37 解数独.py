#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = [set(range(1,10)) for _ in range(9)]
        col = [set(range(1,10)) for _ in range(9)]
        box = [set(range(1,10)) for _ in range(9)]
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] !=".":
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    box[(i//3)*3+j//3].remove(val)
                else:
                    empty.append((i,j))
        def backtrack(iter = 0):
            if iter == len(empty): return True
            i,j = empty[iter]
            b = (i//3) * 3 + j//3
            for val in row[i] & col[j] & box[b]:
                row[i].remove(val)
                col[j].remove(val)
                box[b].remove(val)
                board[i][j] = str(val)
                
                if backtrack(iter+1): return True

                row[i].add(val)
                col[j].add(val)
                box[b].add(val)
            return False

        backtrack()

