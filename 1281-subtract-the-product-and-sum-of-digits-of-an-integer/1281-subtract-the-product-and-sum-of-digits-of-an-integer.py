class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        dig = str(n)
        
        prod = 1
        
        
        for i in range(len(dig)):
            prod *= int(dig[i])
        
        add = [int(x) for x in dig]
        
        res = prod - sum(add)
        
        return res
        