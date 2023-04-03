class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        ans = self.binary(n)
        return ans
    
    def binary(self,bit):
        one = True
        
        if bit & 1 == 0:
            one = False
        length = int.bit_length(bit)
        i = 1
        
        while i < length:
            shift = 1 << i
            val = bit & shift
            
            if (val > 0  and  one) or (val == 0 and not one):
                return False
            
            elif val > 0 and not one:
                one = True
            else:
                one = False
            
            i += 1
            
        return True
        
                
                
            
        
        
        
               
        