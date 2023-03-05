class Solution:
    def baseNeg2(self, n: int) -> str:
        
        
        def recBase2(n):
            if n == 0 or n == 1:
                return str(n)
            
            rem = n % 2
            
            if rem == 0:
                return recBase2(n // -2) + "0"
            else:
                return recBase2((n - 1) // -2) + '1'
            
        
        res = recBase2(n)
        return res