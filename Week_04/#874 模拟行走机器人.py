#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        x,y = 0,0 
        d = 0
        obstacles = set(map(tuple,obstacles))
        ans = 0
        for cmd in commands:
            if cmd == -1: 
                d = (d+1)%4
            elif cmd == -2: 
                d = (d+3)%4
            else:
                for i in range(cmd):
                    if (x+dir[d][0],y+dir[d][1]) not in obstacles:
                        x += dir[d][0]
                        y += dir[d][1]
                        ans = max(ans, x**2+y**2)
        return ans

