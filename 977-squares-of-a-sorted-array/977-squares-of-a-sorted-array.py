class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        square = [pow(x,2) for x in nums]
        
        square.sort()
            
        return square