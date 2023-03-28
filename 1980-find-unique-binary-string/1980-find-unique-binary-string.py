class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        string = "0" * len(nums)
        
        self.binary_string = []
        self.backTracking([], len(nums))
        
        
        
        cont = set(nums)
        
        
        for binary in self.binary_string:
            if binary not in cont:
                return binary
        
            
            
    def backTracking(self, path, n):
        if len(path) == n:
            self.binary_string.append("".join(path))
            return 
        
        path.append("0")
        self.backTracking(path, n)
        path.pop()
        path.append("1")
        self.backTracking(path, n)
        path.pop()
        
    
        