class Solution:
    def isOneBitCharacter(self, bits: list) -> bool:
        last = False
        while(bits):
            if(bits[0] == 1):
                bits[:] = bits[2:]
                last = False
            else:
                bits.pop(0)
                last = True
        return last