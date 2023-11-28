class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def check(value):
            left_offset = max(value - index, 0)
            result = (value + left_offset) * (value - left_offset + 1) // 2
            right_offset = max(value - ((n - 1) - (index)), 0)
            result += (value + right_offset) * (value - right_offset + 1) // 2
            
            return result - value
        
        
        
        maxSum -= n
        l, r = 0, maxSum
        
        while l < r:
            mid = (l + r + 1) // 2
            
            
            if check(mid) <= maxSum:
                l = mid
            else:
                r = mid - 1
                
            
        return l + 1