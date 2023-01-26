class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_val = 0
        
        while left < right:
            
            min_val = min(height[left], height[right])
            cal = min_val * (right - left)
            max_val = max(max_val, cal)
            
            if height[left] < height[right]:
                left += 1
                continue
                
            right -= 1
            
        
        
        return max_val
                
            