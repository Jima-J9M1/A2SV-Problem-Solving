class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        max_val = arr.index(max(arr))
        left = max_val - 1
        right = max_val + 1
        
        if max_val == 0 or max_val == len(arr) - 1:
            return False
        
        if len(arr) < 3:
            return False
        
        while left >= 0:
            
            if arr[left] >= arr[left + 1]:
                return False
            
            left -= 1
        
        while right < len(arr):
            
            if arr[right] >= arr[right - 1]:
                return False
            
            right += 1
            
        return True
