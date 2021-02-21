#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def find(index):
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        def union(index1,index2):
            parent[find(index1)] = find(index2)
        
        provinces = len(isConnected)
        parent = list(range(provinces))
        #print(provinces)
        #print(parent)
        for i in range(provinces):
            for j in range(i+1,provinces):
                if isConnected[i][j] == 1:
                    union(i,j)
        #print(parent)
        circles = sum(parent[i]==i for i in range(provinces))
        return circles

