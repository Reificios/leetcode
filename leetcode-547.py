# problem : There are n cities. Some of them are connected, while some are not. If city a is connected 
#           directly with city b, and city b is connected directly with city c, then city a is connected 
#           indirectly with city c.
#           A province is a group of directly or indirectly connected cities and no other cities outside of 
#           the group.
#           You are given an n x n matrix isConnected where isConnected[i][j] = 1 
#           if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
#           Return the total number of provinces.

from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0 for i in range(len(isConnected))]
        res = 0
        queue = []
        node = 0
        while 0 in visited:
            if(not queue):
                for i in range(len(visited)):
                    if visited[i] == 0:
                        queue.append(i)
                        res += 1
                        break
            node = queue.pop(0)
            if(visited[node] == 0):
                visited[node] = 1
                for i in range(len(isConnected)):
                    if isConnected[node][i] == 1:
                        queue.append(i)
        
        return res