class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        
        fib1 = 0
        fib2 = 1
        fibn = 0
        for _ in range(2,n + 1):
            fibn = fib1 + fib2
            fib1 = fib2
            fib2 = fibn
            
        return fibn
        
        
        
        
        