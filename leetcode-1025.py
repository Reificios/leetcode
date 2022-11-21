from typing import List

class Solution:
    def divisorGame(self, n: int) -> bool:
        if(n == 1):
            return False
        res = [False for i in range(n+1)]
        res[2] = True
        
        for i in range(3,n+1):
            for j in range(1,i//2 +1):
                if i%j == 0 and not res[i-j]:
                    res[i] = True
                    
        return res[n]