class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = [[]]
        self.combination([], 1, comb,k,n)
        
        return comb[0]
    def combination(self, path, idx, comb,k,n):
        if len(path) == k:
            comb[0].append(path)
            return
        
        
        for i in range(idx,n + 1):
            self.combination(path + [i], i + 1, comb, k, n)
            
        
            
        