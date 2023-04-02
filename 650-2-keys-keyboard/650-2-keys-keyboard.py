class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        ans = self.factorization(n)
        
        return ans
        
    def factorization(self,n):
        
        d = 2
        res = []
        
        while d * d <= n:
            
            if n % d == 0:
                res.append(d)
                n //= d
            else:
                d += 1
        
        res.append(n)
        
        return sum(res)
    