class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        
        i = 0
        j = 1
        k = 0
        for _ in range(2,n + 1):
            k = i + j
            i = j
            j = k
            
        return k 
        
        
        
        
        