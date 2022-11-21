from typing import List

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        tmpString = ""
        stack = []
        for i in s:
            if i == "(":
                if stack:
                    tmpString += "("
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    tmpString += ")"
                if not stack:
                    res += tmpString
                    tmpString = ""
        return res