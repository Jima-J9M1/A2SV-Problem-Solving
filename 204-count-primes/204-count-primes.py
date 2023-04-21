class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        
        
        is_prime = [True for _ in range(n + 1)]
        is_prime[0] = False
        is_prime[1] = False
        
        self.sieve_of_era(is_prime, n)
        
        ans = is_prime.count(True)
        
        if is_prime[n] == True:
            ans -= 1
        
        return ans
    
    def sieve_of_era(self, is_prime, n):
        
        divisor = 2
        
        while divisor * divisor <= n:
            
            if is_prime[divisor]:
                div = divisor * divisor
                
                while div <= n:
                    is_prime[div] = False
                    
                    div += divisor
                
            divisor += 1
            
            
        
                