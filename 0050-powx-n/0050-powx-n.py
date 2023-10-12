class Solution:
    def myPow(self, x: float, n: int) -> float:
        base = x
        result = 1
        expo = n
        if expo < 0:
            expo = -n
            
        while expo:
            if expo & 1:
                result *= base
                
            base *= base
            expo >>= 1
            
            
            
        return result if n > 0 else 1/result
        
        
        
        