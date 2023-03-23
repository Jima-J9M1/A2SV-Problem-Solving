class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if max(citations) == 0:
            return 0
                
        
        
        left = 0
        right = len(citations) - 1
        
        while left < right:
            mid = left  + (right - left) // 2
            
            index = ( len(citations) - 1 )  - (mid)
            
            if citations[mid] >= (index + 1):
                right = mid
                
            else:
                left = mid + 1
                
                
        return len(citations) - left