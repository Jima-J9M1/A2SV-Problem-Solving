class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        distinct_prime = [defaultdict(int)]
        ans = 0
        
        for ele in nums:
            self.factorization(ele, distinct_prime)
            
        return len(distinct_prime[0])
    
    def factorization(self, num, distinct_prime):
        d = 2
        res = []
        
        while d * d <= num:
            if num % d == 0:
                distinct_prime[0][d] += 1
                num //= d
            else:
                d += 1
                
        distinct_prime[0][num] += 1
        
        
        
        