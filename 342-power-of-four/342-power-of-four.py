class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 1:
            return False
        
        n /= 4
        ans = self.isPowerOfFour(n)
        return ans