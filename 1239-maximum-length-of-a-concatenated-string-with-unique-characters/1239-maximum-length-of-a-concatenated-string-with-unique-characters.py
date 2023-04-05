class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_count = [0]
        path = set()
        self.backTracking(arr, path , max_count, "", 0)
        
        return max_count[0]
        
    def backTracking(self, arr, path,  max_count, s, idx):
        if len(arr) <= idx:
            if len(s) == len(Counter(s)):
                max_count[0] = max(len(s), max_count[0])
            return 
        
        if len(s) > 0 and len(s) == len(Counter(s)):
            max_count[0] = max(len(s), max_count[0])
            
        elif len(s) > 0 and len(s) != len(Counter(s)):

            return 
        
        
        
        for index in range(idx, len(arr)):
            if arr[index ] not in path:
                
                path.add(arr[index])
                
                self.backTracking(arr, path, max_count, s + arr[index], index + 1)
                path.remove(arr[index])
                
        
        
        