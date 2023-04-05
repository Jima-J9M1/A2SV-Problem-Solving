class Solution:
    def countArrangement(self, n: int) -> int:
        visited = 0
        count = self.backTracking(n, visited, 0)
        
        return count
    
    def backTracking(self,n, visited, bit_count):
        if bit_count == n:
            return 1
        
        count = 0
        for i in range(1, n + 1):
            shift = 1 << (i - 1)
            
            
            if (visited & shift)== 0 and ((bit_count + 1) % i == 0 or (i % (bit_count + 1)) == 0):
                visited |= shift
                count += self.backTracking(n, visited, bit_count + 1)
                visited ^= shift 
            
        return count
                