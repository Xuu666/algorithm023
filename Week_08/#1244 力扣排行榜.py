#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Leaderboard(object):

    def __init__(self):
        self.dic ={}


    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        self.dic[playerId] = self.dic.get(playerId,0) + score


    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        s = sorted([v for v in self.dic.values()], reverse = True)
        return sum(s[:K])


    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        self.dic[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

