class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ans = self.rec(n, k)
        
        return int(ans)
        
        
    def rec(self, n, k):
        if n == 1:
            return "0"
        
        res = self.rec(n - 1, math.ceil(k / 2))
        new_val = ""
        
        if res == "0":
            new_val = "01"
        else:
            new_val = "10"
        
        if k % 2 == 0:
            return new_val[1]
        else:
            return new_val[0]
        
        
        
        
    