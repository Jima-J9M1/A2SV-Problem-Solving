class Solution:
    def countArrangement(self, n: int) -> int:
        visited = set()
        count = self.backTracking(n, visited)
        
        return count
    def backTracking(self,n, visited):
        if len(visited) == n:
            return 1
        
        count = 0
        for i in range(1, n + 1):
            if i not in visited and ((len(visited) + 1) % i == 0 or (i % (len(visited) + 1)) == 0):
                visited.add(i)
                count += self.backTracking(n, visited)
                visited.remove(i)
            
        return count
                