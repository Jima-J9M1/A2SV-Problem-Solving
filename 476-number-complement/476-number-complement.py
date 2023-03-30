class Solution:
    def findComplement(self, num: int) -> int:
        mapp = 1 << (int.bit_length(num))
        
        return (mapp - 1) ^ num