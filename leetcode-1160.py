from typing import List

def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        ans = [0 for i in range(26)]
        for i in chars:
            ans[ord(i) - ord('a')] += 1
        
        count = [0 for i in range(26)]
        passed = True
        for i in words:
            length = len(i)
            passed = True
            for j in range(26):
                count[j] = 0
            for j in range(length):
                char = ord(i[j]) - ord('a')
                count[char] += 1
                if(count[char] > ans[char]):
                    passed = False
                    break
            if passed:
                res += length
                
        return res