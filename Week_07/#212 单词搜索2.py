#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char,{})
            node['#'] = True
       # print(trie)
        def search(i,j,node,pre,visited):
            if "#" in node: res.add(pre)
            for (di,dj) in ((1,0),(0,1),(-1,0),(0,-1)):
                ni, nj = i + di, j + dj
                if -1 < ni < row and -1 < nj < col and board[ni][nj] in node and (ni,nj) not in visited:
                    search(ni, nj, node[board[ni][nj]],pre+board[ni][nj], visited|{(ni,nj)})

        res, row, col = set(), len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] in trie:
                    search(i, j, trie[board[i][j]], board[i][j], {(i, j)})
        return list(res)

