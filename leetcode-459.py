# problem : for string 's' return true if s can be built with only substring of s appending together
#           eg. "abcabcabc" can be build from 3 "abc"s.

from typing import List

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1,len(s) // 2 + 1):
            if(len(s) % i == 0):
                if(s[0:i] * (len(s) // i) == s):
                    return True
        return False