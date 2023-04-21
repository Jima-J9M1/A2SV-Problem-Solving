class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True for _ in range(right + 1)]
        is_prime[0] = False
        is_prime[1] = False
        
        self.sieve_of_era(is_prime, right)
        
        prime_num = []
        
        for num in range(len(is_prime)):
            if is_prime[num] and num >= left:
                prime_num.append(num)
        
        if len(prime_num) <= 1:
            return [-1, -1]
        
        min_val = float("+inf")
        res = []
        
        for indx in range(len(prime_num) - 1):
            diff = prime_num[indx + 1] - prime_num[indx]
            if min_val > diff:
                res = [prime_num[indx], prime_num[indx + 1]]
                min_val = diff
                
        return res
    
    def sieve_of_era(self, is_prime, n):
        
        divisor = 2
        
        while divisor * divisor <= n:
            
            if is_prime[divisor]:
                div = divisor * divisor
                
                while div <= n:
                    is_prime[div] = False
                    
                    div += divisor
                
            divisor += 1