class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def factorization(num1):

            d = 2
            res = set()
            while d * d <= num1:
                if num1 % d == 0:
                    res.add(d)
                    num1 //= d
                else:
                    d += 1
                    
            res.add(num1)
            return res

        count = defaultdict(int)
        
        for ele in deck:
            count[ele] += 1
            
        min_val = min(count.values())
        max_val = max(count.values())
        
        if min_val == 1 :
            return False
        
        prim_factors = factorization(min_val)
        
        flag = True
        
        for prime in prim_factors:
            flag = True
            for ele in count:
                if count[ele] % prime != 0:
                    flag = False
                    break

            if flag:
                break
                    
        if flag:
            return True
        else:
            return False
        
    
    
                