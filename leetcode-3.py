class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLength = 0
        lastCharsInclude = []
        lastLength = 0
        stringLen = len(s)
        curChar = ''

        for i in reversed(range(stringLen)):
            curChar = s[i]
            if curChar in lastCharsInclude:
                j = i+1
                lastCharsInclude = [curChar]
                lastLength = 1
                while(s[j] not in lastCharsInclude):
                    lastCharsInclude.append(s[j])
                    lastLength += 1
                    j += 1
            else:
                lastLength += 1
                lastCharsInclude.append(curChar)
                if(lastLength > longestLength):
                    longestLength = lastLength
        return longestLength

solve = Solution()
# problem = "abcabcbb"
# problem = "bbbbb"
problem = "pwwkew"
print(solve.lengthOfLongestSubstring(problem))