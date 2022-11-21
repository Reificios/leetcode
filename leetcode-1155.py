from typing import List

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        res = [[0 for i in range(target+1)] for i in range(n+1)]
        for i in range(1,n+1):
            if i == 1:
                until = k if k < target else target
                for j in range(until):
                    res[i][j+1]=1
            for j in range(target):
                for v in range(1,k+1):
                    if(j+v <= target and i+1 <= n):
                        res[i+1][j+v] += res[i][j]
        # print(res[n])
        return res[n][target] % (10**9+7)
