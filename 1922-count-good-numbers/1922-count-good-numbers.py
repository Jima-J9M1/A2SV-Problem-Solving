class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        if n % 2 == 1:
            cal = math.ceil(n / 2)
            cal2 = math.floor(n / 2)
            
            res1 = pow(5, cal, 1_000_000_007)
            res2 = pow(4, cal2, 1_000_000_007)
            
            result  = res1 * res2
        else:
            cal = math.ceil(n / 2)
            res1 = pow(5, cal, 1_000_000_007)
            res2 = pow(4, cal, 1_000_000_007)
            
            result = res1 * res2
            
        return result % 1_000_000_007
        
        