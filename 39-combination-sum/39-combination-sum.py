class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.target = target
        self.backTracking(candidates, [], 0, 0)
        
        return self.ans
    
    def backTracking(self, candidates, path, idx, add):
        
        if add == self.target:
            self.ans.append(path[:])
            return 
        
        if  add > self.target:
            return 
        
        
        for i in range(idx, len(candidates)):
            path.append(candidates[i])
            self.backTracking(candidates, path, i, add + candidates[i])
            val = path.pop()
            
            
        
        