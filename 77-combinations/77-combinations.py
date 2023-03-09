class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backTracking(idx, arr):
            if len(arr) == k:
                ans.append(arr[:])
                return
            
            if idx > n:
                return
    
            for i in range(idx, n+1):
                arr.append(i)
                backTracking(i+1, arr)
                arr.pop()
        
        backTracking(1, [])
        return ans