#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res=[]
        def help(root):
            if not root:
                return
            res.append(root.val)
            for children in root.children:
                help(children)
        help(root)
        return res

