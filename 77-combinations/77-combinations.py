class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1,n+1)]
        ans = []
        
        def backTracking(idx, arr):
            if len(arr) == k:
                ans.append(arr[:])
                return
            
            if idx >= len(nums):
                return
    
            for i in range(idx,len(nums)):
                arr.append(nums[i])
                backTracking(i+1, arr)
                arr.pop()
        
        backTracking(0, [])
        return ans