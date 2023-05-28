class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci = {0:0}
        for i in range(1, n + 1):
            if i <= 2:
                trib = 1
            else:
                trib = tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3]
                
            tribonacci[i] = trib
            
        return tribonacci[n]